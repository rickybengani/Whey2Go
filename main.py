from flask import Flask, redirect, url_for, render_template, request, session
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret"

train_df = pd.read_csv('./interactions_train.csv')

@app.route('/', methods=["POST", "GET"])
def home():
    # Code to generate non-personalized recipes #
    non_personalized = ['Pizza', 'Pasta', 'Tacos', 'Burger', 'Naan', 'Queso', 'Shwarma', 'Salad', 'Fried Rice', 'Cake']
    # Code to generate non-personalized recipes #
    if request.method == "POST":
        ratings = request.form.getlist("ratings[]")
        session["ratings"] = ratings
        return redirect(url_for("personalized"))
    else:
        return render_template("nonpersonalized.html", non_personalized=non_personalized)


@app.route("/personalized")
def personalized():
    if "ratings" in session:
        ratings = session["ratings"]
        # Code to generate personalized recipes #
        personalized = ratings
        # Code to generate personalized recipes #
        
        return render_template("personalized.html", personalized=personalized)


if __name__ == "__main__":
    app.run(debug=True)