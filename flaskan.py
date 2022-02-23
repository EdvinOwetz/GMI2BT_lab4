from flask import Flask,render_template,request
# from flask import request


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
        #print(formdata)
        #return data
        return render_template("return_form.html",data=formdata)
    else:
        return "Wrong method, no GET only POST!"


# @app.route('/shortenurl', methods=['GET', 'POST'])
# def shortenurl():
#     if request.method == 'POST':
#         return render_template('shortenurl.html', shortcode=request.form['shortcode'])
#     elif request.method == 'GET':
#         return 'A GET request was made'
#     else:
#         return 'Not a valid request method for this route'

if(__name__=="__main__"):
    print("Starting Flask")
    app.run()