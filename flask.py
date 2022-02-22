from flask import Flask, render_template
from flask import request


__author__="Edvin Owetz, Nils Broberg"

app=Flask(__name__)

#POST
#@app.route("/",methods=["POST"])
@app.route("/")
def display_form():
    return "Hello"
#    return render_template("./web_form/index.html")

if(__name__=="__main__"):
    print("Starting Flask")
    app.run()