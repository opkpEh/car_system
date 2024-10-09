# app.py
from flask import Flask, render_template
import random
import json

app = Flask(__name__)

with open('static/cars.json', 'r') as cars_list:
    cars = json.load(cars_list)

with open('static/reviews.json', 'r') as review_list:
    reviews = json.load(review_list)

with open('static/new_cars.json', 'r') as new_cars_list:
    new_cars = json.load(new_cars_list)

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

    return render_template('new_cars.html', new_cars=new_cars)

if __name__ == '__main__':
    app.run(debug=True)