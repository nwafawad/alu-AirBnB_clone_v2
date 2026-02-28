# Web Flask

A Flask web application for the AirBnB clone project.

## Overview

This module implements a web interface using Flask to serve the AirBnB clone application, providing routes for displaying listings, user interactions, and dynamic content rendering.

## Features

- Dynamic HTML templating with Jinja2
- RESTful API endpoints
- Static file serving (CSS, JavaScript, images)
- Database integration with SQLAlchemy

## Installation

```bash
pip install flask
```

## Usage

```python
from web_flask import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## Project Structure

```
web_flask/
├── __init__.py
├── static/
├── templates/
└── views/
```

## Routes

Configure your Flask routes in the views module to handle GET/POST requests for the application.

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
