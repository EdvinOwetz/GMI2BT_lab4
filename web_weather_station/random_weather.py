from flask import request
from random import uniform

def generate_weather_data():
    weather_data = {}
    weather_data["data"] = []
    for i in range(100,110):
        weather_data["data"].append({"Time":i,"Temp":round(uniform(-10.0,20.0),1),"Humidity":round(uniform(5.0,99.0),1),"Pressure":round(uniform(1025.0,1090.0),2)})
    return weather_data

print(generate_weather_data())