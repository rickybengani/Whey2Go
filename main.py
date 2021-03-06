from flask import Flask, redirect, url_for, render_template, request, session
import pandas as pd
import numpy as np
import math

app = Flask(__name__)
app.secret_key = "secret"

# train_df = pd.read_csv('./interactions_train.csv')
personalized_df = pd.read_csv('./personalized.csv')
personalized_df[['temp1', 'Recipe', 'temp2']] = personalized_df['Recipe'].str.split("\'", expand=True)
personalized_df = personalized_df.drop(['temp1', 'temp2'], axis=1)
# print(personalized_df.head())
top_recipes_df = pd.read_csv('./top_recipes.csv')
combined_df = pd.merge(top_recipes_df, personalized_df, how='inner', left_on='RecipeName', right_on='Recipe')
combined_df = combined_df.drop(['RecipeID', 'RecipeName'], axis=1)

@app.route('/')
def home():
    return render_template("layout.html")

@app.route("/nonpersonalized", methods=["POST", "GET"])
def nonpersonalized():
    # Code to generate non-personalized recipes #
    non_personalized = []
    for i in range(10):
        non_personalized.append(combined_df['Recipe'].iloc[i])
    print(non_personalized)
    # non_personalized = ['Pizza', 'Pasta', 'Tacos', 'Burger', 'Naan', 'Queso', 'Shwarma', 'Salad', 'Fried Rice', 'Cake']
    # Code to generate non-personalized recipes #
    if request.method == "POST":
        ratings = request.form.getlist("ratings[]")
        session["ratings"] = ratings
        session["non_personalized"] = non_personalized
        return redirect(url_for("personalized"))
    else:
        return render_template("nonpersonalized.html", non_personalized=non_personalized)

@app.route("/personalized")
def personalized():
    if "ratings" in session and "non_personalized" in session:
        ratings = session["ratings"]
        non_personalized = session["non_personalized"]
        arrays = []
        # Code to generate personalized recipes #
        for i in range(len(ratings)):
            if (int(ratings[i]) > 0):
                ind = personalized_df[personalized_df['Recipe'] == non_personalized[i]].index
                personalized = personalized_df.iloc[ind].to_numpy()
                personalized = personalized[personalized != math.nan]
                personalized = personalized[~pd.isnull(personalized)]
                personalized = np.delete(personalized, 0)
                arrays.append(personalized)

        # Code to generate personalized recipes #
        
        return render_template("personalized.html", personalized=arrays, size=personalized.size)


if __name__ == "__main__":
    app.run(debug=True)