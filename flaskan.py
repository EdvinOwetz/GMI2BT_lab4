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
def form_recive():
    # lista=[]
    # lista.append(request.form["fname"])
    # lista.append(request.form["ename"])
    # lista.append(request.form["kort"])
    # text=""
    # for item in lista:
    #     text+=item+"\n"
    # return text

    return str(request.get_json())

    #return render_template("return_form.html",data=data)
    #return render_template('shortenurl.html', shortcode=request.form['shortcode'])


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