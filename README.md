# Sample Math API

This project implements a REST API for basic mathematical operations (logarithm, root, power, and factorial) using [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/). Below are the steps to get the project up and running.

## Purpose

This project serves as a **test task** for QA engineers. It is designed to help them test API endpoints, validate error handling, and explore API documentation generated with the [OpenAPI Specification (OAS)](https://swagger.io/specification/).

The project is set up with [SQLite](https://www.sqlite.org/index.html) as the default database for development purposes, which provides a simple, file-based solution with no need for complex database setup.

## Requirements

- **Python 3.11+**: The project is written in [Python](https://www.python.org/doc/), so you need the correct version installed to run it.
- **Git**: Used for cloning the project from GitHub.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Deeplace/sample-math-api
    cd test-math-api
    ```
    - This command downloads the project files from GitHub to your local machine and navigates into the project folder. You only need to do this once to get the source code.

2. **Install dependencies using Poetry**:
    ```bash
    poetry install
    ```
    - [Poetry](https://python-poetry.org/) is a tool for managing Python project dependencies. This command reads the `pyproject.toml` file and installs all necessary libraries (e.g., [Django](https://pypi.org/project/Django/), [Django REST Framework](https://pypi.org/project/djangorestframework/)). Poetry will also create a virtual environment to isolate these dependencies from your system Python packages.

3. **Apply migrations**:
    ```bash
    poetry run python src/manage.py migrate
    ```
    - Django uses migrations to create and modify database tables. This command runs any pending migrations, setting up the SQLite database for use. You need to do this once (or after changing models).

4. **Create a superuser for the Django admin**:
    ```bash
    poetry run python src/manage.py createsuperuser
    ```
    - This command creates an admin user who can access the Django admin panel. It will prompt you for a username, email, and password. You need to create this user only once to gain access to administrative features.
    - The Django admin page can be accessed by visiting the following URL:
        ```
        /admin/
        ```

        - This page provides a user-friendly interface for managing the application's data and performing administrative tasks. You can log in using the superuser credentials created in step 4 of the installation process.

5. **Activate the virtual environment and run the development server**:
    ```bash
    poetry run python src/manage.py runserver
    ```
    - This command starts the Django development server, allowing you to interact with the API locally. You need to run this command every time you want to start the server.

## Documentation

This project uses [`drf-spectacular`](https://drf-spectacular.readthedocs.io/en/latest/readme.html) and the [OpenAPI Specification (OAS)](https://swagger.io/specification/) for generating API documentation. The documentation allows you to understand the structure and behavior of the API, including available endpoints and their input/output formats.

- To download the latest `openapi.json` file (which contains the full API schema in JSON format), visit the following URL:
    ```
    /api/schema/
    ```
- Documentation is also accessible through the Django admin panel. After logging in (into admin account), you can click the **"Documentation"** button in the top menu to view the API structure.

## Additional Information

- You only need to clone the repository, install dependencies, and set up the database once. These steps prepare your local environment for development.
- You need to run the development server each time you want to test or develop the project. Running migrations is necessary only when changes to the database schema occur (e.g., after adding or modifying models).
