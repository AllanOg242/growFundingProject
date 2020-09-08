from flask import Blueprint
hopital = Blueprint('hopital', __name__)
from . import views, errors


