from weather import get_weather
from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/weather")
def get_weather_condition():
    city = request.args.get('city')    #get args from form. retrive the value
    current_weather_data = get_weather(city)
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city="Barrie"

    #City is not found by API
    if not current_weather_data['cod'] ==200:
        return render_template("city-not-found.html")

    return render_template(
        "weather.html",
        title = current_weather_data["name"],
        status = current_weather_data["weather"][0]["description"].capitalize(),
        feels_like = f"{current_weather_data['main']['feels_like']:.1f}",
        temp = f"{current_weather_data['main']['temp']:.1f}"
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
    # app.run(host="0.0.0.0", port=8000,debug=True, use_reloader=True)