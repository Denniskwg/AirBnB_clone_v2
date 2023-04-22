#!/usr/bin/python3
"""2-c_route  starts a Flask web application
application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask, escape
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
