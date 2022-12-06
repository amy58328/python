import socket 
from threading import Thread
import time
import datetime
import json
import math
from PoseHandler import PoseHandler

g_socket_server = None  
 
g_conn_pool = {}  #儲存client IP

g_client_type_pool = {}#儲存對應IP的權限

recieve_time_list = []  #紀錄每個封包接收花費時間

packet_size = 1024   #預設封包大小

ContentEnd = True #分割msg判斷是否完整

poseHandler = PoseHandler()

def init():
    #now = datetime.datetime.now().strftime("%H:%M:%S.%f") 
    # hostname = socket.gethostname()
    # ip = socket.gethostbyname(hostname)
    # print('server ip address:',ip)
    # ADDRESS = ('172.16.53.12',8713)#('172.16.53.12', 8713)#('140.124.182.79', 8712) 
    ADDRESS = ('127.0.0.1',8713)
    global g_socket_server, packet_size
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)  
    print("server start, wait for client connecting...")

def accept_client():#接收新连接
    while True:
        client, info = g_socket_server.accept() 
        #print(client) 
        #print(info)
        thread = Thread(target=message_handle, args=(client, info))#開一個thread專門負責
        thread.setDaemon(True)
        thread.start()
 
def message_handle(client, info):
    client.sendall("connect server successfully!".encode(encoding='utf8'))
    temp_msg = ""
    cmd_connect = True
    while cmd_connect:
        try:
            bytes = client.recv(packet_size)
            recieve_time = datetime.datetime.now()
            #print(recieve_time)
            msg = bytes.decode(encoding='utf8')
            
            while msg != "" and msg !="123123":
                msg, temp_msg = slice_msg(msg , temp_msg)
                #print('slice:',temp_msg ,"and", msg)
                #print(temp_msg)
                #if checkJSON(temp_msg):
                if ContentEnd == True:
                    jd = json.loads(temp_msg) 

                    client_id = jd['client_id']     # client device id
                    device_type = jd['device_type'] # client device type
                    client_type = jd['client_type'] # client type : isMaster = true or false
                    cmd = jd['cmd']                 # client command
                    joint_list = jd['joint_list']   # joint list from master
                    client_send_time = jd['sendTime']   # recieve time from client

                    #print(client_send_time)
                    show_recieve_time(client_send_time,recieve_time,client_id,device_type)
                    write_time_list_cs(client_send_time,recieve_time,client_id,device_type)
 
                    if  cmd == "CONNECT":  #client首次進行連線
                        g_conn_pool[client_id] = client
                        g_client_type_pool[client_id] = client_type
                        jd['joint_list'] = poseHandler.GetPose()
                        jd['cmd'] = "SEND_DATA"
                        jmsg = json.dumps(jd)
                        SendPoseToSlave(jmsg)
                        print('on client connect: id =' , client_id , ",device type =", device_type ,",isMaster =", client_type,",cmd =", cmd, joint_list) #info
                        #print("client_send_time",client_send_time)

                    elif cmd == "DISCONNECT":  #client中斷連線
                        cmd_connect = False
                        print("disconnect",client_id)
                        remove_client(client_id)
                        break

                    elif cmd == 'SEND_DATA': #單筆傳送
                        #print('recv client msg from ' + client_id + ":", client_type, cmd, joint_list)
                        poseHandler.SetPose(joint_list)#設定角度同步
                        SendPoseToSlave(temp_msg)#傳送joint_list給client
                        poseHandler.TransformPose(joint_list,'0')#傳送joint_list給手臂
                    
                    elif cmd == 'AUTO_SEND_DATA': #連續傳送
                        #print('recv client msg from ' + client_id + ":", client_type, cmd, joint_list)
                        poseHandler.SetPose(joint_list)#設定角度同步
                        SendPoseToSlave(temp_msg)#傳送joint_list給client
                        poseHandler.TransformPose(joint_list,'1')#傳送joint_list給手臂

                    elif cmd == 'MASTER_REQUEST': #deal with master request
                        print('client',client_id,'request master')
                        master_id = GetMasterID()
                        switchMaster(client_id,master_id,temp_msg)

                    elif cmd == 'MASTER_REPLY': #Synchronize joint_list
                        print('Synchronize joint_list')
                        SendRequestToMaster(temp_msg)

                    elif cmd == 'ACTIVE_GRAB':
                        print('recieve grab commend')

                    else:
                        print('error command')    

                    temp_msg = ""

        except Exception as e:
            print(e)
            #print(msg)
            print(len(msg))
            #print(jd)
            remove_client(client_id)
            break

def SendPoseToSlave(msg):
    for client_id in g_conn_pool:
        if not(g_client_type_pool[client_id]):#加入判斷不傳master
            send_client_time = datetime.datetime.now()
            g_conn_pool[client_id].sendall(msg.encode(encoding='utf8'))
            #g_conn_pool[client_id].sendall(bytes)
            wrtie_time_list_sc(send_client_time)

def SendRequestToMaster(msg):
    for client_id in g_conn_pool:
        if g_client_type_pool[client_id]:#只傳給master
            send_client_time = datetime.datetime.now()
            g_conn_pool[client_id].sendall(msg.encode(encoding='utf8'))
            #g_conn_pool[client_id].sendall(bytes)
            wrtie_time_list_sc(send_client_time)

def GetMasterID():#回傳Master ID
    for client_id in g_client_type_pool:
        if g_client_type_pool[client_id]:
            return client_id
    return False

def switchMaster(client_id,master_id,msg):#交換master和client權限
    if  master_id != False:
        SendRequestToMaster(msg)
        g_client_type_pool[client_id] = True
        g_client_type_pool[master_id] = False
        print("master",master_id,"switch to slave")
    else:
        g_client_type_pool[client_id] = True
    print("client",client_id,"switch to master")
     
def checkJSON(msg):#檢查JSON是否完整
    if len(msg) != packet_size:
        print(msg)
        return False
    elif msg.find("{") != 0:
        print(msg)
        return False
    else:
        return True

def slice_msg(msg,temp_msg):
    global ContentEnd
    #print('original_msg:',msg)
    #print('original_temp_msg:',temp_msg)
    if len(temp_msg) == 0:
        ContentEnd = True
    else:
        ContentEnd = False

    if ContentEnd == True:  #temp裡面沒有東西
        if msg.find('{') != -1:
            ContentEnd = False  #若找到第一個{則代表msg尚未結束        
            temp_msg = msg[msg.find('{') : ]
            #print('temp_msg:',temp_msg)

            if temp_msg.find('}') != -1:
                ContentEnd = True   #若找到第一個}則代表msg已經結束   
                msg = temp_msg[temp_msg.find('}')+1 : ] #msg去掉}以前的訊息
                temp_msg = temp_msg[ : temp_msg.find('}')+1] #temp_msg拿取第一組{}的訊息
                #print('msg:',msg)
                #print('temp_msg:',temp_msg)
                #print('slice',slice_msg(msg,""))
            else:
                msg = ""
                
    else:
        if msg.find('}') != -1: #msg裡面有結束符號
            ContentEnd = True
            temp_msg = temp_msg + msg[ : msg.find('}')+1] #原始temp_msg加上msg}前的訊息
            msg = msg[msg.find('}')+1 : ] #msg去掉}以前的訊息
            #print('msg:',msg)
            #print('temp_msg:',temp_msg)
            #print('slice',slice_msg(msg,""))

        else:   #msg裡面沒有結束符號
            temp_msg = temp_msg + msg
            msg = ""
            #print('temp_msg:',temp_msg)
    #print("return",ContentEnd)
    return msg, temp_msg

def show_recieve_time(client_send_time,recieve_time,client_id,device_type):
    client_send_time = datetime.datetime.strptime(client_send_time, '%Y-%m-%d %H:%M:%S.%f')
    tcp_latency = (recieve_time - client_send_time).total_seconds()
    print('recieve msg time = ', tcp_latency ,'sec')
    global recieve_time_list 
    recieve_time_list.append(tcp_latency) 
    

def write_time_list_cs(client_send_time,recieve_time,client_id,device_type):#client->server
    cst = datetime.datetime.strptime(client_send_time,'%Y-%m-%d %H:%M:%S.%f')
    time_info = "[server],[client->server]," + device_type + ',' + client_id + ',' + "null," + str(cst)  + ',' + str(recieve_time)
    with open("server_recieve_time_list.txt", 'a') as f:
        f.writelines(time_info+'\n')
        f.close()

def wrtie_time_list_sc(server_send_time):#server->client
    time_info = "[server],[server->client],null," + server_send_time.strftime('%Y-%m-%d %H:%M:%S.%f')  + ',null' 
    with open("server_send_time_list.txt", 'a') as f:
        f.writelines(time_info+'\n')
        f.close()

def remove_client(client_id):
    client = g_conn_pool[client_id]
    print('remove_client',client)
    if None != client:
        client.close()
        g_conn_pool.pop(client_id)
        g_client_type_pool.pop(client_id)
        print("client offline: " + client_id)
        print('average recieve time =',round( sum(recieve_time_list) / len(recieve_time_list), 6), 'sec')

if __name__ == '__main__':
    init()
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    while True:
        time.sleep(0.002)
