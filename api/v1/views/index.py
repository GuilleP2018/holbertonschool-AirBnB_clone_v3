#!/usr/bin/python3
""" Starts a Flask web application """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns a JSON """
    return jsonify({"status": "OK"})


@app_views.route('/hello', strict_slashes=False)
def hello():
    """ Another route example """
    return jsonify({"message": "Hello, Flask!"})
