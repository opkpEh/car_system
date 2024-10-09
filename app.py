# app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

cars = [
    {
        "id": 1,
        "name": "Luxury Sedan",
        "make": "Mercedes-Benz",
        "model": "E-Class",
        "year": 2023,
        "price": 54000,
        "mileage": 1500,
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "available": True,
        "image": "https://images.unsplash.com/photo-1567818735868-e71b99932e29?auto=format&fit=crop&q=80&w=800&h=600",
        "description": "Experience ultimate luxury with this sleek Mercedes-Benz E-Class. Featuring cutting-edge technology and supreme comfort, this sedan is perfect for both city driving and long journeys."
    },
    {
        "id": 2,
        "name": "Family SUV",
        "make": "Toyota",
        "model": "Highlander",
        "year": 2022,
        "price": 35000,
        "mileage": 15000,
        "fuel_type": "Hybrid",
        "transmission": "Automatic",
        "available": True,
        "image": "https://images.unsplash.com/photo-1716068072348-64c2b7181161?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8VG95b3RhJTIwSGlnaGxhbmRlciUyMGNhcnxlbnwwfHwwfHx8MA%3D%3D",
        "description": "The perfect family vehicle, this Toyota Highlander offers ample space, excellent fuel efficiency with its hybrid engine, and top-notch safety features to keep your loved ones secure."
    },
    {
        "id": 3,
        "name": "Compact Hatchback",
        "make": "Volkswagen",
        "model": "Golf",
        "year": 2021,
        "price": 22000,
        "mileage": 28000,
        "fuel_type": "Gasoline",
        "transmission": "Manual",
        "available": False,
        "image": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.hgmsites.net%2Fhug%2F2019-toyota-corolla_100648053_h.jpg&f=1&nofb=1&ipt=9f29f712d58abf33025d061fb2d8c8b690bbface54f77de5cf3f32df5534e140&ipo=images",
        "description": "This Volkswagen Golf is the ideal city car. Its compact size makes parking a breeze, while its efficient engine ensures great fuel economy. Perfect for the urban commuter."
    },
    {
        "id": 4,
        "name": "Sports Car",
        "make": "Porsche",
        "model": "911",
        "year": 2023,
        "price": 120000,
        "mileage": 500,
        "fuel_type": "Gasoline",
        "transmission": "Automatic",
        "available": True,
        "image": "https://images.unsplash.com/photo-1610915504025-d806f0041582?auto=format&fit=crop&q=80&w=800&h=600",
        "description": "Feel the thrill of the road with this stunning Porsche 911. With its powerful engine and precise handling, this sports car offers an unparalleled driving experience for enthusiasts."
    },
    {
        "id": 5,
        "name": "Electric Sedan",
        "make": "Tesla",
        "model": "Model 3",
        "year": 2023,
        "price": 45000,
        "mileage": 1000,
        "fuel_type": "Electric",
        "transmission": "Automatic",
        "available": True,
        "image": "https://images.unsplash.com/photo-1560958089-b8a1929cea89?auto=format&fit=crop&q=80&w=800&h=600",
        "description": "Embrace the future of driving with this Tesla Model 3. Featuring long-range battery capacity, autopilot capabilities, and zero emissions, this electric car is both eco-friendly and cutting-edge."
    }
]
# Sample reviews
reviews = [
    {"author": "John D.", "content": "Great selection of cars! The buying process was smooth and easy.", "rating": 5},
    {"author": "Sarah M.", "content": "I found my dream car here. The staff was very helpful.", "rating": 4},
    {"author": "Mike R.", "content": "Good prices and excellent customer service.", "rating": 5},
    {"author": "Emily L.", "content": "The website is user-friendly and informative. Highly recommend!", "rating": 4},
]


@app.route('/')
def home():
    # Random car-related image for carousel
    carousel_images = [
        "https://images.unsplash.com/photo-1606664919413-9c73fb5464db?auto=format&fit=crop&q=80&w=800&h=600",
        "https://images.unsplash.com/photo-1610915504025-d806f0041582?auto=format&fit=crop&q=80&w=800&h=600",
        "https://images.unsplash.com/photo-1567818735868-e71b99932e29?auto=format&fit=crop&q=80&w=800&h=600"
    ]

    # Featured cars (based on a dynamic selection)
    featured_cars = random.sample(cars, 3)

    return render_template('home.html', carousel_images=carousel_images, reviews=reviews, featured_cars=featured_cars)

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
        {"name": "Electric Car E", "price": 40000, "image": "https://images.unsplash.com/photo-1469285994282-454ceb49e63c?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"name": "Hybrid Car F", "price": 30000, "image": "https://plus.unsplash.com/premium_photo-1686730540270-93f2c33351b6?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
        {"name": "Luxury Sedan G", "price": 60000, "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGx1eGFyeSUyMGNhciUyMGZ1bGwlMjBib2R5fGVufDB8fDB8fHww"},
    ]
    return render_template('new_cars.html', new_cars=new_cars)

if __name__ == '__main__':
    app.run(debug=True)
