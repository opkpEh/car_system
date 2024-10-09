from flask import Flask, render_template, request, redirect, url_for
import random
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


with open('static/cars.json', 'r') as cars_list:
    cars = json.load(cars_list)

with open('static/reviews.json', 'r') as review_list:
    reviews = json.load(review_list)


@app.route('/')
def home():
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


@app.route('/upload_car', methods=['GET', 'POST'])
def upload_car():
    if request.method == 'POST':
        if 'car_image' not in request.files:
            return 'No file uploaded', 400

        file = request.files['car_image']
        if file.filename == '':
            return 'No file selected', 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_car = {
                'id': len(cars) + 1,
                'name': request.form['car_name'],
                'details': request.form['car_details'],
                'price': float(request.form['car_price']),
                'image': f'uploads/{filename}',
                'available': True
            }

            cars.append(new_car)

            # Save updated cars list to JSON file
            with open('static/cars.json', 'w') as f:
                json.dump(cars, f, indent=4)

            return redirect(url_for('available_cars'))

    return render_template('upload_car.html')


@app.route('/compare_cars', methods=['GET', 'POST'])
def compare_cars():
    available = [car for car in cars if car['available']]

    if request.method == 'POST':
        car1_id = int(request.form['car1'])
        car2_id = int(request.form['car2'])

        car1 = next((car for car in cars if car['id'] == car1_id), None)
        car2 = next((car for car in cars if car['id'] == car2_id), None)

        return render_template('compare_cars.html', cars=available, car1=car1, car2=car2)

    return render_template('compare_cars.html', cars=available)


if __name__ == '__main__':
    app.run(debug=True)