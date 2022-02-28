from random import randint, uniform
from datetime import datetime

def generate_weather_data() -> list[dict]:
    weather_data = []
    
    for i in range(20):
        weather_data.append({
                            "Device": "Random Device",
                            "Location": "60.65661396854781, 15.337069653989222",
                            "Time": str(datetime(2020,2,14,i)),
                            "Temp": round(uniform(-10.0, 20.0), 1),
                            "Humidity": round(uniform(5.0, 99.0), 1),
                            "Pressure": round(uniform(1025.0, 1090.0), 2)
                            })
    return weather_data