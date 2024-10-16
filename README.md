# User Management System

A User Management System built with Python and FastAPI that allows for the management of user data with CRUD operations. This application utilizes SQLAlchemy for database interactions, Pydantic for data validation, and FastAPI for creating robust API endpoints.

## Features

- **User Registration**: Create new user accounts.
- **User Authentication**: Securely log in and manage sessions.
- **CRUD Operations**: Create, Read, Update, and Delete user data.
- **API Endpoints**: Expose RESTful APIs for user management.
- **Templating**: Render dynamic HTML pages using Jinja2.
- **Testing**: Comprehensive unit and integration tests using FastAPI's TestClient and Pytest.

## Technologies Used

- **Python**: Programming language used for building the application.
- **FastAPI**: Modern web framework for building APIs with Python 3.6+.
- **SQLAlchemy**: ORM for database operations.
- **MySQL**: Relational database management system for storing user data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **FastAPI TestClient**: Testing HTTP requests in FastAPI.
- **Pytest**: Framework for writing simple and scalable test cases.
- **Jinja2**: Templating engine for rendering HTML pages.
- **Uvicorn**: ASGI server for running FastAPI applications.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- MySQL Server
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/emignardi/ums.git
   cd ums

2. **Create and Activate Virtual Environment:**

    python -m venv venv
    ./venv/Scripts/activate.bat

3. **Install Required Dependencies:**

    pip install -r requirements.txt

4. **Create Database and Update database.py Configuration:**

    CREATE DATABASE ums;
    CREATE DATABASE ums_test;

5. **Run the Application:**

## API Documentation

- http://127.0.0.1:8000/docs

## Authors

- [@emignardi](https://github.com/emignardi)

![screenshot](/images/index.png)
![screenshot](/images/create.png)
![screenshot](/images/update.png)
