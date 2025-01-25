from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("data.csv")
    parks_data = df.to_dict('records')

    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 25))

    start = (page - 1) * per_page
    paginated_parks = parks_data[start:start + per_page]

    has_next = (start + per_page) < len(parks_data)
    has_prev = start > 0

    return render_template(
        "index.html",
        parks=paginated_parks,
        page=page,
        per_page=per_page,
        has_next=has_next,
        has_prev=has_prev
    )

@app.route("/about")
def about():
    df = pd.read_csv("data.csv")
    parks_data = df.to_dict('records')  
    total_parks = len(parks_data) 

    return render_template("about.html", total_parks=total_parks)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    df = pd.read_csv("data.csv")
    df = df.fillna("") 
    parks_data = df.to_dict('records')

    query = request.args.get("query", "").lower()
    if query:

        filtered_parks = [
            park for park in parks_data 
            if query in str(park['title']).lower() or query in str(park['desc']).lower()
        ]
    else:
        filtered_parks = parks_data 

    return render_template("search.html", parks=filtered_parks, query=query)


if __name__ == "__main__":
    app.run(debug=True)