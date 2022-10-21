"""
A common Flask pattern is to define the start-up logic for the Flask server in this file.
The start-up logic is responsible for locating and applying any app configuration, 
and getting the server ready to receive requests.
"""

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    return app