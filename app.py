from flask import Flask
from flask import render_template
import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/parks")
def parks():
    df = pd.read_csv("data.csv")
    parks = df.to_dict('records')
    
    return render_template(
        'index.html',
        parks=parks
    )

@app.route("/parks/<int:park_id>")
def park_detail(park_id):
    df = pd.read_csv("data.csv")
    matching_rows = df[df['park_code'] == park_id]

    if matching_rows.empty:
        return "Park not found", 404

    park = matching_rows.to_dict('records')[0]

    return render_template(
        'parks.html',
        park=park
    )

@app.route("/powerplants/<int:plant_id>")
def powerplant_detail(plant_id):
    return f"You are looking for the power plant with ID {plant_id}"