import paho.mqtt.client as mqtt
import time
#Connack: MQTT Connect Acknowledgment Packet
def on_connect(client,userdata,flags,rc):
    print("Connected with the result code "+str(rc))
    #client.subscribe([("esp8266/weatherS",0),("esp8266/temperature",0),("esp8266/humidity",0),("esp8266/pressure",0),("esp8266/gas",0),("esp8266/altitude",0)])
    client.subscribe("esp8266/#")
#def on_message(client,userdata,msg):
#    print(msg.topic+""+str(msg.payload))

def weatherSCallback(client,userdata,msg):
    global weatherSBuffer
    weatherSBuffer=msg.payload.decode("utf-8")
    #print(weatherSBuffer)
    
def humidityCallback(client,userdata,msg):
    global humidityBuffer
    humidityBuffer=msg.payload.decode("utf-8")

def pressureCallback(client,userdata,msg):
    global pressureBuffer
    pressureBuffer=msg.payload.decode("utf-8")

def gasCallback(client,userdata,msg):
    global gasBuffer
    gasBuffer=msg.payload.decode("utf-8")

def altitudeCallback(client,userdata,msg):
    global altitudeBuffer
    altitudeBuffer=msg.payload.decode("utf-8")

def temperatureCallback(client,userdata,msg):
    global temperatureBuffer
    temperatureBuffer=msg.payload.decode("utf-8")

broker_address="cpsiot.cs.uni-kl.de"
client=mqtt.Client()
#

client.message_callback_add("esp8266/weatherS",weatherSCallback)
client.message_callback_add("esp8266/pressure",pressureCallback)
client.message_callback_add("esp8266/humidity",humidityCallback)
client.message_callback_add("esp8266/gas",gasCallback)
client.message_callback_add("esp8266/altitude",altitudeCallback)
client.message_callback_add("esp8266/temperature",temperatureCallback)
client.connect(broker_address,1883,60)    

client.loop_start()
#client.on_message=on_message
#client.message_callback_add("esp8266/temperature",temperature)
#client.message_callback_add("esp8266/humidity",humidity)
#client.on_connect=on_connect
client.subscribe("esp8266/#")
time.sleep(4)
#client.loop_stop()
#client.loop_forever()
#print(weatherSBuffer)
#print(pressureBuffer)
#print(humidityBuffer)