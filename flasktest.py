from flask import Flask, jsonify, request
import mqttConnection as data
import ThingDescriptor as TDesc
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

oid="dc1b778c-2f48-0647-a488-ecfbfbde7a12"



@app.route('/objects') ##ta sciezkei musisz zmienic na bank!!
def get_info():
  return jsonify(TDesc.thing_descriptor())

@app.route('/device/'+oid+'/property/humidity')
def get_humidity():
  return jsonify(data.humidityBuffer)
  
@app.route('/device/'+oid+'/property/gas')
def get_gas():
  return jsonify(data.gasBuffer)

@app.route('/device/'+oid+'/property/temperature')
def get_temperature():
  return jsonify(data.temperatureBuffer)

@app.route('/device/'+oid+'/property/altitude')
def get_altitude():
  return jsonify(data.altitudeBuffer)
@app.route('/device/'+oid+'/property/pressure')
def get_pressure():
  return jsonify(data.pressureBuffer)
@app.route('/device/'+oid+'/property/weather')
def get_weather():
  return data.weatherSBuffer


