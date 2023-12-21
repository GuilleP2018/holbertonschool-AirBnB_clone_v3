#!/usr/bin/python3
"""
views init file
"""
from api.v1.views.index import *
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
