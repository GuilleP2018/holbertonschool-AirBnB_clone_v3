#!/usr/bin/python3
""" starts a Flask web application """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """returns a JSON"""
    return jsonify({"status": "OK"})
