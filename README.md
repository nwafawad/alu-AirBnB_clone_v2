# AirBnB Clone v2

## Description
This is a Python-based implementation of an AirBnB clone, featuring object-oriented design and persistent data storage.

## Features
- Command-line interface (CLI) for user interaction
- Object-oriented architecture with serialization
- Data persistence using JSON
- Support for various model types (User, Place, City, etc.)

## Installation
```bash
git clone <repository-url>
cd alu-AirBnB_clone_v2
```

## Usage
```bash
./console.py
```

Enter commands to interact with the application:
- `create <class>` - Create a new object
- `show <class> <id>` - Display an object
- `all [class]` - List all objects
- `destroy <class> <id>` - Delete an object
- `update <class> <id> <attribute> <value>` - Update an object

## Project Structure
```
.
├── models/          # Data models
├── tests/           # Unit tests
├── console.py       # Main CLI application
└── README.md
```

## Requirements
- Python 3.x

## Authors
See CONTRIBUTORS or git log for details.