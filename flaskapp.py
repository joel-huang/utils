# export FLASK_APP=flaskapp.py, flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == 'main':
	app.run(host='0.0.0.0')