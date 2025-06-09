from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "77f72c5445de619f7356af387decc1bd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.form['city']
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'].title()
            }
        else:
            error = "City not found :("

    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)