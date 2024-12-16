pip freeze > requirements.txt
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
        parks=parks) 

if __name__ == '__main__':
    app.run(debug=True)


