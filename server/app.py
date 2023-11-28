#!/usr/bin/env python3

from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)  
    return f"{parameter}"


@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter + 1))
    return f"{numbers}"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1,num2,operation):
 result=None

 if operation == '+':
    result = num1 + num2
 elif operation == '-':
    result = num1 - num2
 elif operation == '*':
    result = num1 * num2
 elif operation == 'div':
    num2 != 0
    result = num1 / num2
 elif operation == '%':
    result = num1 % num2

    if result == None:
       return 'invalid or less then 0'
    
 return str(result)

 


    

 if __name__ == '__main__':
    app.run(port=5555, debug=True)
