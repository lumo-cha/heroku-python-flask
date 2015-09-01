from flask import *

app = Flask(__name__)
app.config.from_object("config")

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World"

@app.route("/config", methods=["GET"])
def config():
    results = {kvpair[0]: str(kvpair[1]) for kvpair in app.config.items() }
    return jsonify(results)

