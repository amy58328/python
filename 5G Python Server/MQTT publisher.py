import paho.mqtt.client as mqtt
import json


def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("connect to MQTT Broker")
    else:
        print("faild to connect to MQTT broker, return code %d\n",rc)


print("create client")
client = mqtt.Client()

print("set username password")
client.username_pw_set("james04","0404xx")

# set callback function 
client.on_connect = on_connect

print("connect to server ")
client.connect("140.124.201.124",1883)



print("create sented message")
message = {"command":[0,"f",[0,0,0,0,0,0]]}

print("sent message to server")
client.publish("AGV move",json.dumps(message))