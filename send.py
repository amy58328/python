import time
import paho.mqtt.client as mqtt
import os
import struct
import pandas as pd 

def on_connect(client, userdata, flags, rc):
    print("Connect with result "+str(rc))
  
def on_message(client, userdata, msg):
    print("接收到的消息为:"+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_messafe = on_message
client.username_pw_set("james01","0101xx")
client.connect('140.124.182.78', 1883)
client.loop_start()
path = "1.png"

if os.path.exists(path):
    #图片存在，发送图片
    filepath = path
    if os.path.isfile(filepath):
        # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
        fileinfo_size = struct.calcsize('128sl')
        # 定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl', bytes(os.path.basename(filepath).encode('utf-8')),os.stat(filepath).st_size)
        print(os.stat(filepath).st_size)
        client.publish('Pi-1', payload = fhead, qos =0)
        time.sleep(3)
        filesize=os.stat(filepath).st_size
       
        print ('client filepath: {0}'.format(filepath))
        
        fp = open(filepath, 'rb')
        re_size=0
        while 1:
            if filesize - re_size >= 1024:  #文件切片，大小可自定义，视情况而定
                data = fp.read(1024)
                re_size += 1024
            else:
                data = fp.read(filesize -  re_size)
                print(len(data))
            if not data:
                print ('{0} file send over...'.format(filepath))
                print('')
                break
            client.publish('Pi-1', payload = data, qos =0)
    
        time.sleep(1)
# else:
#     break

client.loop_stop()
print('Photos send end.')
print('Server is receiving, wait patiently please !')