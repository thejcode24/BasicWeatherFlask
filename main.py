from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    # Get the input value from input form with name 'zip' as zipcode
    zipcode = request.form['zip']

    # Get the current weather data from OpenWeatherMap API using input zipcode.
    # According to OWM API docs, country code defaults to USA so works for my small scale purposes.
    # TODO: Add exception handling for bad inputs, first get working model running.

    r = requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zipcode+",us&appid=6652e6f0e87b109f51468c98d43b67b3")
    r_json = r.text
    return r_json
    # return render_template("temperature.html")

@app.route('/')
def index():
    return render_template("index.html")

if __name__  == "__main__":
    app.run(debug=True)