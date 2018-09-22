from flask import Flask, jsonify, request
import mqttConnection as data
import ThingDescriptor as TDesc
import http
import json
import _thread
import time
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app_port = 5001

#oid="weatherstation-infrastructure-name"

def temperaturePublish():
  previous_temperature=-100
  while(True):
    try:
      connection=http.client.HTTPConnection("127.0.0.1",port=9997)
      #print(connection)
      rheaders={"infrastructure-id":"weatherstation-infrastructure-name","adapter-id":"my-weather-station"}
      if(data.temperatureBuffer!=previous_temperature):
        temperature_event={"temperature":data.temperatureBuffer}
        j_body=json.dumps(temperature_event)
        str_body=str(j_body)
        print(str_body)
        connection.request(method='PUT',url='/agent/events/weather-station-temperature',body=str_body,headers=rheaders)
        response = connection.getresponse()
        print(response.status)
        previous_temperature=data.temperatureBuffer
        time.sleep(10)
    except:
      print("Agent is not started or can't connect to it")
      time.sleep(5)


_thread.start_new_thread(temperaturePublish,())

@app.route('/objects') ##tu jest thing descriptor
def get_info():
  return jsonify(TDesc.thing_descriptor())

@app.route('/device/<oid>/property/humidity')
def get_humidity(oid):
  humJson={"humidity":data.humidityBuffer}
  return jsonify(humJson)
  
@app.route('/device/<oid>/property/gas')
def get_gas(oid):
  gasJson={"gas":data.gasBuffer}
  return jsonify(gasJson)

@app.route('/device/<oid>/property/temperature')
def get_temperature(oid):
  temperatureJson={"temperature":data.temperatureBuffer}
  return jsonify(temperatureJson)

@app.route('/device/<oid>/property/altitude')
def get_altitude(oid):
  altitudeJson={"altitude":data.altitudeBuffer}
  return jsonify(altitudeJson)
@app.route('/device/<oid>/property/pressure')
def get_pressure(oid):
  pressureJson={"pressure":data.pressureBuffer}
  return jsonify(pressureJson)
@app.route('/device/<oid>/property/weather')
def get_weather(oid):
  return data.weatherSBuffer


app.run(port=app_port)