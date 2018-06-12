import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

class City(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


@app.route('/')
def index():
    cities = City.query.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d29e532297d901144394a2faf99e31ca'
    
    weather_data = []

    for city in cities:
        
         r = requests.get(url.format(city.name)).json()
         
         weather = {
            'city': city.name,
            'temperature': round(r['main']['temp']),
            'description': r['weather'][0]['description'],
            'humidity': r['main']['humidity'],
            'icon': r['weather'][0]['icon']
         }
         weather_data.append(weather)

    print(weather)
    return render_template('weather.html', weather_data=weather_data)