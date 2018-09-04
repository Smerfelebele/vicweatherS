from flask import Flask, jsonify, request
import mqttConnection as data
import ThingDescriptor as TDesc
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

oid="dc1b778c-2f48-0647-a488-ecfbfbde7a12"



@app.route('/objects') ##tu jest thing descriptor
def get_info():
  return jsonify(TDesc.thing_descriptor())

@app.route('/device/'+oid+'/property/humidity')
def get_humidity():
  humJson={"humidity":data.humidityBuffer}
  return jsonify(humJson)
  
@app.route('/device/'+oid+'/property/gas')
def get_gas():
  gasJson={"gas":data.gasBuffer}
  return jsonify(gasJson)

@app.route('/device/'+oid+'/property/temperature')
def get_temperature():
  temperatureJson={"temperature":data.temperatureBuffer}
  return jsonify(temperatureJson)

@app.route('/device/'+oid+'/property/altitude')
def get_altitude():
  altitudeJson={"altitude":data.altitudeBuffer}
  return jsonify(altitudeJson)
@app.route('/device/'+oid+'/property/pressure')
def get_pressure():
  pressureJson={"pressure":data.pressureBuffer}
  return jsonify(pressureJson)
@app.route('/device/'+oid+'/property/weather')
def get_weather():
  return data.weatherSBuffer


