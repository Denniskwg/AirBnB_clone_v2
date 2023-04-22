#!/usr/bin/python3
"""3-python_route starts a Flask web application
application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    var = escape(text)
    var = var.replace('_', ' ')
    return "C {}".format(var)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_iscool(text="is_cool"):
    var = escape(text)
    var = var.replace('_', ' ')
    return "Python {}".format(var)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if type(n) is int:
        return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
