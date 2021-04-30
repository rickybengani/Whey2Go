# Whey2Go
Whey2Go is a recipe recommender system that recommends both non-personalized and personalized recipes.

## Instructions to Run the Flask Web App

1. Clone the repository.
2. Run the following commands to install the required packages (if not already installed).

```bash
pip install flask
pip install numpy
```

3. Run the following command to start the web app on localhost.

```bash
python "main.py"
```

## Instructions to Rerun the Python Notebook

1. Open the Whey2Go-Recommender folder to access the Whey2Go-Recommender.ipynb file.
2. Add the following files from https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions to the same directory:
- interactions_train.csv
- RAW_recipes.csv
3. Run the notebook all the way through. This will generate the files used in the Flask web app. These files, however, have already been generated and stored in this repo:
- top_recipes.csv
- personalized.csv
