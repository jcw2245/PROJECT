from flask import Flask
from flask import render_template
import pandas as pd


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

#@app.route("/parks")
#def parks():
    #df = pd.read_csv("parks.csv")
    #parks = df.to_dict('records') 
    
   # return render_template(
        #'parks.html',
        #parks=parks
#    ) 

if __name__ == '__main__':
    app.run(debug=True)

