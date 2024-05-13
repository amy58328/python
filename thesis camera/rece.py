import paho.mqtt.client as mqtt
import numpy as np
import pandas as pd 
import time
import threading
import sys
import os
import struct
import csv

count = 0
Tag = 0
Tag_2 = 0
new_filename = 0
filesize = 0
fp = 0
writer = 0

new_filename = os.path.join('../IMG.jpg')
fp = open(new_filename, 'wb') 

def on_connect(client, userdata, flags, rc):
    print("Connect with result: "+str(rc))

def on_message(client, userdata, msg):
    global new_filename,filesize,fp,writer,Tag

    if msg.topic == "IMG":
        # print(msg.payload)

        fp.write(msg.payload)
        if fp.tell() >= filesize:
            print(f"filesize = {filesize}")
            Tag = 0
            print('1 Round over.')
            fp.close()
            time.sleep(1)
            #接收完成，Tag置为2
            Tag = 2
    if msg.topic == "IMG_SIZE":
        # global filesize
        
        filesize = int(msg.payload)
        # print(filesize)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("james01","0101xx")
client.connect('140.124.182.78', 1883)
client.subscribe([('Pi-1',2),('IMG_SIZE',2)])
client.loop_start()

print('start')

while True:
    if (Tag == 2):
        client.publish('Rece', payload = bytes(('OK').encode('UTF-8')), qos =0)
        #print('end')
        #break
    else:
        pass