from flask import Flask,abort,request, jsonify
import json
import http.client
import thingdescriptor as TDescVAS


adapter_id = "value-added-service-ws"


#consumption of events
#popraw jeszcze thing descriptor!

app=Flask(__name__)

@app.route('/objects')
def get_info():
    return jsonify(TDescVAS.thingDescriptor())

@app.route('/objects/WeatherStationToLampService/events/<eid>',methods=['PUT'])
def rcv_event_endpoint(eid):
    connection= http.client.HTTPConnection("127.0.0.1", port=8181)
    str_payload = str(request.data,"utf-8")
    j_payload = json.loads(str_payload)
    print(j_payload)
    print(connection.getresponse())

