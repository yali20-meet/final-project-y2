from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template("index.html")

@app.route('/recomendation')
def reco_route():
	return render_template("recommendations.html")

if __name__ == '__main__':
    app.run(debug=True, port=9000)