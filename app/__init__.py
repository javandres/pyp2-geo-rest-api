# encoding: utf-8
"""
Example RESTful API Server.
"""
from flask import Flask
from flask_restplus import Resource, Api
from flask_cors import CORS, cross_origin

api_v1 = Api(
    version='1.0',
    title="LlactaLab | REST GeoAPI",
    description=(
        "This is a Geospatial REST API.\n\n"
    ),
)

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    # Initialize the Flask-App
    app = Flask(__name__, **kwargs)

    # Enable CORS
    cors = CORS(app)

    # Load the config file
    app.config.from_object('config.DevelopmentConfig')

    # Initialize FLASK-RESTPlus
    api_v1.init_app(app)

    # Initialize the modules
    from . import modules
    modules.init_app(app)

    return app