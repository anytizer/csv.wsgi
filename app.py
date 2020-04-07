from flask import Flask, Response, render_template, request
import json
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/test", methods=["GET"])
@app.route("/test/", methods=["GET"])
def get_index_test():
    data = {"message": "It works"}
    output = json.dumps(data)
    return output


@app.route("/server", methods=["GET"])
@app.route("/server/", methods=["GET"])
def get_server():
    output = str(datetime.datetime.now())
    return output


@app.route("/parse", methods=["POST"])
@app.route("/parse/", methods=["POST"])
def post_parse():
    table = request.form["table"]
    csv = [row.split("\t") for row in request.form["csv"].splitlines()]
    output = f"Dumping CSV Data into <strong>`{table}`</strong>: "+str(csv)
    return output
