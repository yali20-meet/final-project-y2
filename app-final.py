from flask import Flask, render_template
from flask import request

from database import *

app = Flask(__name__)

@app.route('/' , methods=["GET" , "POST"])
def home_route():
	if request.method == "GET":
		return render_template("index.html")
	else:
		companyName = request.form["companyName"]
		email = request.form["email"]
		companyInfo = request.form["companyInfo"]
		add_company(companyName , email , companyInfo)
		return render_template("answer.html")

@app.route('/recommendation')
def reco_route():
	return render_template("recommendations.html")

@app.route('/vick')
def vick_route():
    return render_template("vick.html")
    

if __name__ == '__main__':
    app.run(debug=True, port=8076)
