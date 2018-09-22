from flask import Flask,abort,request, jsonify
import json
import http.client
import thingdescriptor as TDescVAS
import _thread
from datetime import date

adapter_id = "value-added-service-ws"


#consumption of events
#popraw jeszcze thing descriptor!

def lamp_property_change(temp_value):
    day_of_year = date.today().timetuple().tm_yday
    if(day_of_year>=121 and day_of_year<274):
        season="summer"
    else:
        season="winter"

    if(season=="summer"):
        if(temp_value>30):
            brightness=int(round(((temp_value-30)*100)/(10)))
            brightness_str=str(brightness)
            data={"value": "0,100,"+brightness_str}  #red  
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        elif(temp_value>25 and temp_value<=30):
            brightness=int(round(((temp_value-25)*100)/(5)))
            brightness_str=str(brightness)
            data={"value": "35,100,"+brightness_str} #orange
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        elif(temp_value>15 and temp_value<=25):
            brightness=int(round(((temp_value-15)*100)/(10)))
            brightness_str=str(brightness)
            data={"value": "121,100,"+brightness_str} #green
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        else:
            data={"value": "234,100,100"} #blue
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
    else:
        if(temp_value>15 and temp_value<=25):
            brightness=int(round(((temp_value-15)*100)/(10)))
            brightness_str=str(brightness)
            data={"value": "0,100,"+brightness_str}  #red  
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        elif(temp_value>10 and temp_value<=15):
            brightness=int(round(((temp_value-10)*100)/(5)))
            brightness_str=str(brightness)
            data={"value": "35,100,"+brightness_str} #orange
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        elif(temp_value>3 and temp_value<=10):
            brightness=int(round(((temp_value-3)*100)/(7)))
            brightness_str=str(brightness)
            data={"value": "121,100,"+brightness_str} #green
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
        else:
            data={"value": "234,100,100"} #blue
            j_body=json.dumps(data)
            str_body=str(j_body)
            print(str_body)
    connection=http.client.HTTPConnection("127.0.0.1",port=9997)
    print("values")
    rheaders={"infrastructure-id":"WeatherStationToLampService","adapter-id":"value-added-service-ws"}             
    connection.request('PUT','/agent/remote/objects/da494aa6-dc83-416c-86c9-8fb2f289274f/properties/WeatherBulb_Color',headers = rheaders, body = str_body)
    response=connection.getresponse()
    print(response)
    '''data_dimmer={"value":"20"} #sciemniacz
    j_dimmerbody=json.dumps(data_dimmer)
    str_dimmerbody=str(j_dimmerbody)
    connection.request('PUT','/agent/remote/objects/da494aa6-dc83-416c-86c9-8fb2f289274f/properties/WeatherBulb_Dimmer',headers = rheaders, body = str_dimmerbody)
    print("Task finished")'''


app=Flask(__name__)

@app.route('/objects')
def get_info():
    return jsonify(TDescVAS.thingDescriptor())

@app.route("/objects/WeatherStationToLampService/events/weather-station-temperature",methods=['PUT'])
def rcv_event_endpoint():
    print("start")
    #connection= http.client.HTTPConnection("127.0.0.1", port=9997)
    str_payload = str(request.data,"utf-8")
    j_payload = json.loads(str_payload)
    value=float(j_payload["temperature"])
    #value=14.0
    print(type(value))
    _thread.start_new_thread(lamp_property_change,(value,))
    print("stop")
    return("ok")
