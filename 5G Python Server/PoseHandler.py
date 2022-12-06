from doctest import master
import math
import time
import json
import rtde_control
import rtde_receive
import serial
import numpy as np
import warnings
import socket

real_connect = False    #實體手臂是否連接

if real_connect:
    rtde_c = rtde_control.RTDEControlInterface("192.168.49.130")#實體手臂"192.168.50.7"#10.1.1.130
    rtde_r = rtde_receive.RTDEReceiveInterface("192.168.49.130")#實體手臂"192.168.50.7"#10.1.1.130

    #pose = [0.3209,-0.11057,0.17505,2.23,-2.2195,0]#實體手臂
    #rtde_c.moveL(pose)#實體手臂

    pose = [0,-90,-90,-90,90,0]
    pose_to_arm = [pose[0]*(math.pi/180),pose[1]*(math.pi/180),pose[2]*(math.pi/180),pose[3]*(math.pi/180),pose[4]*(math.pi/180),pose[5]*(math.pi/180)]
    rtde_c.moveJ(pose_to_arm)#實體手臂
    print("----------------------------------------1-------------------------------------")
    print(rtde_r.getTargetQ())
    print(rtde_r.getActualQ())
    print(rtde_r.getActualTCPPose())
    print(rtde_r.getTargetTCPPose())
    print("----------------------------------------2-------------------------------------")

velocity = 0.05
acceleration = 0.05
dt = 1.0/500  # 2ms
lookahead_time = 0.1
gain = 300

class PoseHandler:
    def __init__(self):
        self.currentPose = [0,-90,-90,-90,90,0]
        self.master = ""

    def GetPose(self):
        #print("getPOSE:",self.currentPose)
        return self.currentPose

    def SetPose(self, pose):
        #print("setPOSE:",pose)
        self.currentPose = pose

    def TransformPose(self, splitPacket,mode):
        #start = time.time()
        if(mode == "1"):#連續傳送
            pose = [(float)(splitPacket[0]),(float)(splitPacket[1]),(float)(splitPacket[2]),(float)(splitPacket[3]),(float)(splitPacket[4]),(float)(splitPacket[5])]
            pose_to_arm = [pose[0]*(math.pi/180),pose[1]*(math.pi/180),pose[2]*(math.pi/180),pose[3]*(math.pi/180),pose[4]*(math.pi/180),pose[5]*(math.pi/180)]
            #self.SetPose(pose)
            if real_connect:
                rtde_c.servoJ(pose_to_arm, velocity, acceleration, dt, lookahead_time, gain)#實體手臂
            #end = time.time()
            #duration = end - start
            # if duration < dt:
            #     time.sleep(dt - duration)
                
        elif(mode == "0"):#單筆傳送
            pose = [(float)(splitPacket[0]),(float)(splitPacket[1]),(float)(splitPacket[2]),(float)(splitPacket[3]),(float)(splitPacket[4]),(float)(splitPacket[5])]
            pose_to_arm = [pose[0]*(math.pi/180),pose[1]*(math.pi/180),pose[2]*(math.pi/180),pose[3]*(math.pi/180),pose[4]*(math.pi/180),pose[5]*(math.pi/180)]
            #self.SetPose(pose)
            if real_connect:
                rtde_c.moveJ(pose_to_arm)#實體手臂
            
        else:
            print("Error Code")
            print("----------------------------------------1-------------------------------------")
        print(rtde_r.getTargetQ())
        print(rtde_r.getActualQ())
        print(rtde_r.getActualTCPPose())
        print(rtde_r.getTargetTCPPose())
        print("----------------------------------------2-------------------------------------")