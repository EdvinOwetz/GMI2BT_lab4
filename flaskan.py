from flask import Flask, render_template, request
import random_weather
import requests

import json

__author__ = "Edvin Owetz, Nils Broberg"

app = Flask(__name__)

# POST
# @app.route("/",methods=["POST"])


@app.route("/form")
def display_form():
    return render_template("index.html")


@app.route("/submit", methods=["POST", "GET"])
def show_form_data():
    if request.method == "POST":
        # data är nu en dictionary (ImmutableDictionary) oförändelig dictionary
        formdata = request.form
        print(formdata)
        # return data
        return render_template("return_form.html", data=formdata)
    else:
        return "Wrong method, no GET only POST!"


@app.route("/getweather", methods=["POST"])
def get_weather_json():
    if request.method == "POST":
        data:list[dict] = random_weather.generate_weather_data()
        ret_data:dict={"datakeys":list(data[0].keys()),"data":data}
        return ret_data
    else:
        error="call to get_weather_json : Error : Wrong method, only POST!"
        print(error)
        return error


@app.route("/weather")
def show_weather():
    result = requests.post("http://127.0.0.1:5000/getweather")
    
    #print("This is the Data Gathered in Show Weather")
    #print(result)
    if result.status_code == 200:
        # print("This is Json data:")
        # print(result)
        return render_template("return_weather.html", data=result.json())
    else:
        error = f"Failed to retrive data. status code: {result.status_code} ."
        print(error)
        return error


if(__name__ == "__main__"):
    print("Starting Flask")
    app.run()
