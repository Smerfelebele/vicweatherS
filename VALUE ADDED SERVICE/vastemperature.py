from flask import Flask,abort,request, jsonify
import json
import http.client
import thingdescriptor as TDescVAS
import _thread

adapter_id = "value-added-service-ws"


#consumption of events
#popraw jeszcze thing descriptor!

def lamp_property_change(value):
    connection=http.client.HTTPConnection("127.0.0.1",port=9997)
    print("values")
    rheaders={"infrastructure-id":"WeatherStationToLampService","adapter-id":"value-added-service-ws"}
    data={"value": "30,30,30"}
    j_body=json.dumps(data)
    str_body=str(j_body)
    print(str_body)
    connection.request('PUT','/agent/remote/objects/da494aa6-dc83-416c-86c9-8fb2f289274f/properties/WeatherBulb_Color',headers = rheaders, body = str_body)
    response=connection.getresponse()
    print(response)
    print("Task finished")


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
    print(type(value))
    _thread.start_new_thread(lamp_property_change,(value,))
    print("stop")
    return("ok")
