#!/usr/bin/python3
""""""

from flask import jsonify
from api.v1.views import app_views


if __name__ == "__main__":
    pass  # Add any additional logic if required


@app_views.route('/status', strict_slashes=False)
def status():
    """returns a JSON"""
    return jsonify({"status": "OK"})


