#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:string_param>')
def print_string(string_param):
    print(string_param)
    return string_param


@app.route('/count/<int:count_param>')
def count(count_param):
    result = '\n'.join(str(i) for i in range(count_param)) + '\n'
    return result


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        result = 'Unknown operation'
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
