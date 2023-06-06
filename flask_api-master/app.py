from flask import Flask
from flask import render_template
import requests # pip install Flask requests

app = Flask(__name__)

# Load the index page
@app.route("/", methods=["GET", "POST"])
def index():
    # Make a request to the PokeAPI
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    # if there is an api key, append it to the url with '?api_key=' like this:
    # response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu" + "?api_key=" + api_key)

    # Convert the response to JSON
    data = response.json()

    # Extract the image URL from the data
    image = data["sprites"]["front_default"]

    # Extract the name from the data
    name = ""

    # Render the index.html template with the image URL sent as a argument and provide <img> tag with the image URL
    return render_template("index.html", image=image, name=name)

if __name__ == "__main__":
    app.run(debug=True)