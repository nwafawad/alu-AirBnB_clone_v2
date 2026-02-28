#!/usr/bin/python3
"""
Module for a basic Flask web application.

This script initializes a Flask server that listens on 0.0.0.0:5000
and exposes three routes:

    /           - Returns the string 'Hello HBNB!'
    /hbnb       - Returns the string 'HBNB'
    /c/<text>   - Returns 'C <text>' with underscores replaced by spaces
"""

from flask import Flask

# Initialize the Flask application instance
# __name__ helps Flask determine the root path for resources
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Handles requests to the root URL (/).

    Returns:
        str: A simple 'Hello HBNB!' greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles requests to the /hbnb URL.

    Returns:
        str: The string 'HBNB'.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays a string starting with 'C ' followed by the value of the text
    parameter provided in the URL.

    The route automatically replaces underscores (_) in the text with spaces
    to improve readability when displaying the result.

    Args:
        text (str): The dynamic URL parameter representing a word or phrase.
                    Any underscores in this value are converted to spaces.

    Returns:
        str: A formatted string in the form 'C <text>' where <text> is the
             processed version of the URL parameter.
    """
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


if __name__ == "__main__":
    # Start the Flask development server.
    # Host : 0.0.0.0 - listen on all available network interfaces
    # Port : 5000    - standard Flask default port
    app.run(host='0.0.0.0', port=5000)
