# app.py
from flask import Flask, render_template
import random
import json

app = Flask(__name__)

with open('static/cars.json', 'r') as cars_list:
    cars = json.load(cars_list)

with open('static/reviews.json', 'r') as review_list:
    reviews = json.load(review_list)

#with open('static/new_cars.json', 'r') as new_cars_list:
#   new_cars = json.load(new_cars_list)

@app.route('/')
def home():

    # Featured cars (based on a dynamic selection)
    featured_cars = random.sample(cars, 3)

    return render_template('home.html', reviews=reviews, featured_cars=featured_cars)

@app.route('/available_cars')
def available_cars():
    available = [car for car in cars if car['available']]
    return render_template('available_cars.html', cars=available)

@app.route('/buy_car/<int:car_id>')
def buy_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        car['available'] = False
    return render_template('buy_car.html', car=car)

@app.route('/new_cars')
def new_cars():
    new_cars = [
        {
            "name": "Electric Car E",
            "price": 40000,
            "image": "https://images.unsplash.com/photo-1469285994282-454ceb49e63c?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        },
        {
            "name": "Hybrid Car F",
            "price": 30000,
            "image": "https://plus.unsplash.com/premium_photo-1686730540270-93f2c33351b6?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        },
        {
            "name": "Luxury Sedan G",
            "price": 60000,
            "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGx1eGFyeSUyMGNhciUyMGZ1bGwlMjBib2R5fGVufDB8fDB8fHww"
        }
    ]
    return render_template('new_cars.html', new_cars=new_cars)

if __name__ == '__main__':
    app.run(debug=True)