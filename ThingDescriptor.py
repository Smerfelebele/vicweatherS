import json
from flask import jsonify, request

def thing_descriptor():
    td = {
    "adapter-id": "my-weather-station",
    "thing-descriptions":[
    {

    "oid": "weatherstation-infrastructure-name",
    "name": "weatherstation",
    "type": "adapters:Thermometer",
	"version": "0.0.1",
	"keywords": [],
    "properties": [
        {
            "pid": "temperature",
            "monitors": "adapters:AmbientTemperature",
            "read_link": {
                "href": "/device/{oid}/property/{pid}",
                "output": {
                    "type": "object",
                    "field":[
                        {
                            "name": "value",
                            "schema": {
                                 "units": "Celsius",
                                 "type": "double"
                            }
                        }
                    ]
                }
           
			}
		
			},
               {
            "pid": "humidity",
            "monitors": "adapters:AverageHumidity",
            "read_link": {
                "href": "/device/{oid}/property/{pid}",
                "output": {
                    "type": "object",
                    "field":[
                        {
                            "name": "value",
                            "schema": {
                                "units": "percent",
                                 "type": "double"
                            }
                        }
                    ]
                }
           
			}
		
			},
               {
            "pid": "altitude",
            "monitors": "adapters:AverageHumidity",
            "read_link": {
                "href": "/device/{oid}/property/{pid}",
                "output": {
                    "type": "object",
                    "field":[
                        {
                            "name": "value",
                            "schema": {
                                "units": "meters",
                                 "type": "double"
                            }
                        }
                    ]
                }
           
			}
		
			},
               {
            "pid": "gas",
            "monitors": "adapters:AverageHumidity",
            "read_link": {
                "href": "/device/{oid}/property/{pid}",
                "output": {
                    "type": "object",
                    "field":[
                        {
                            "name": "value",
                            "schema": {
                                "units": "percent",
                                 "type": "double"
                            }
                        }
                    ]
                }
           
			}
		
			},
               {
            "pid": "pressure",
            "monitors": "adapters:AverageHumidity",
            "read_link": {
                "href": "/device/{oid}/property/{pid}",
                "output": {
                    "type": "object",
                    "field":[
                        {
                            "name": "value",
                            "schema": {
                                "units": "hPa",
                                 "type": "double"
                            }
                        }
                    ]
                }
           
			}
		
			}

		
				
    ],
    "actions": [],
    "events": [{
            "eid": "weather-station-temperature",
            "monitors": "adapters:AmbientTemperature",
            "output": {
                "type": "object",
                "field":[
                        {
                            "name": "value",
                            "schema": {
                                 "units": "Celsius",
                                 "type": "double"
                            }
                        }
                    ]
            }
        }]
    }
    ]
    }
    return td
