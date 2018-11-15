"""
To run this app, in your terminal:
> export FLASK_ENV=development
> export FLASK_APP=flask_demo.py
> flask run

Navigate to
> http://127.0.0.1:5000/
> http://127.0.0.1:5000/predict/5
> http://127.0.0.1:5000/predict/11
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/predict/<int:number>')
def predict(number):
    if number < 10:
         return "I predict that " + str(number) + " is less than 10!"
    else:
        # Using a value greater than 10 will generate an error
        # Use the information in the debugger to fix the problem
        return "I predict that " + number + " is greater than or equal to 10!"
