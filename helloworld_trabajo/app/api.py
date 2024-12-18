import http.client

from flask import Flask

from app import util
from app.calc import Calculator

CALCULATOR = Calculator()
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}


@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        # Convert input parameters to numbers
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        
        # Perform multiplication
        result = CALCULATOR.multiply(num_1, num_2)
        
        # Return the result with OK status
        return ("{}".format(result), http.client.OK, HEADERS)
    except TypeError as e:
        # Return an error message with BAD_REQUEST status if conversion fails
        return (str(e), http.client.BAD_REQUEST, HEADERS)

@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        # Convert input parameters to numbers
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        
        # Check for division by zero
        if num_2 == 0:
            # Return 406 for division by zero
            return ("Cannot divide by zero", 406, HEADERS)
        
        # Perform division
        result = CALCULATOR.divide(num_1, num_2)
        
        # Return the result with OK status
        return ("{}".format(result), http.client.OK, HEADERS)
    except TypeError as e:
        # Return an error message with BAD_REQUEST status if conversion fails
        return (str(e), http.client.BAD_REQUEST, HEADERS)
