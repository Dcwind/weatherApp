import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d29e532297d901144394a2faf99e31ca'
    city = 'Bangkok'
    
    
    r = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': round(r['main']['temp']),
        'description': r['weather'][0]['description'],
        'humidity': r['main']['humidity'],
        'icon': r['weather'][0]['icon']
    }
    print(weather)
    return render_template('weather.html')