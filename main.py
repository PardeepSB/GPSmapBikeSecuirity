import json
from flask import Flask
from flask import render_template, jsonify

app = Flask(__name__)

@app.route('/data_json')
def data_json():
    f = open("Coordinates.csv", "r")
    latLongt = f.read().split(",") 
    lat = float(latLongt[0])
    longt = float(latLongt[1])
    f.close
    dummy_data = [
        {
            "id": 1,
            "lat": lat,
            "longt": longt,
        },
    ]
    return jsonify(dummy_data)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/map')
def map():
    dummy_data = data_json()

    return render_template('map.html', map=dummy_data.json)