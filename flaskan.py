from flask import Flask,render_template,request
import random_weather
import requests

__author__="Edvin Owetz, Nils Broberg"

app=Flask(__name__)

#POST
#@app.route("/",methods=["POST"])
@app.route("/form")
def display_form():
    return render_template("index.html")

@app.route("/submit",methods=["POST","GET"])
def show_form_data():
    if request.method == "POST":
        #data är nu en dictionary (ImmutableDictionary) oförändelig dictionary
        formdata=request.form
        print(formdata)
        #return data
        return render_template("return_form.html",data=formdata)
    else:
        return "Wrong method, no GET only POST!"

@app.route("/getweather",methods=["GET"])
def show_weather_json():
    r=request.json
    print(r)
    return random_weather.generate_weather_data()

@app.route("/weather")
def show_weather():
    #result=requests.request.get("127.0.0.1:5000/getweather")
    result=random_weather.generate_weather_data()
    print(result)
    return render_template("return_weather.html",data=result["data"])


if(__name__=="__main__"):
    print("Starting Flask")
    app.run()