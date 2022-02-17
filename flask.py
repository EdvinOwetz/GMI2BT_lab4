from flask import Flask
from flask import request


__author__="Edvin Owetz, Nils Broberg"

app=Flask(__name__)

#POST
@app.route("/action/submit",methods=["POST"])
def display_form():
    pass

if(__name__=="__main__"):
    print("Starting Flask")
    app.run()