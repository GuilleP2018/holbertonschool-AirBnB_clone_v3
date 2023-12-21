# api/v1/views/index.py

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/status', strict_slashes=False)
def status():
    """returns a JSON"""
    return jsonify({"status": "OK"})
from api.v1.views import app_views
