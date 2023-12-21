#!/usr/bin/python3
"""
Return status of API
"""

from flask import Flask
import os
from models import storage

app = Flask(__name__)
f
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Close storage"""
    storage.close()

if __name__ == "__main__":
    HBNB_API_HOST = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    HBNB_API_PORT = int(os.getenv('HBNB_API_PORT', default='5000'))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
from api.v1.views import app_views