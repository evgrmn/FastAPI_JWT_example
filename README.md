# JWT authentication example for FastAPI with Pytest testing
![](https://badgen.net/badge/Python/3.10/blue) ![](https://badgen.net/badge/FastAPI/0.95.2/gray) ![](https://badgen.net/badge/Pytest/7.2.1/blue) ![](https://badgen.net/badge/Pydantic/1.10.8/gray) ![](https://badgen.net/badge/Poetry/0.1.0/blue)

## What is inside

- [ ] A simple example of a service for viewing the current salary of company employees

- [ ] The database of company employees is located in the text file *app/database/fake_users_db.json*

- [ ] Viewing information from the database is possible with a password

- [ ] JSON Web Token (JWT) authentication technology

- [ ] Using the dependency manager Poetry

- [ ] Running a service in an isolated Docker container

- [ ] Pytest Autotests

- [ ] The code is based on the official FastAPI documentation [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Implementation

- [ ] The API has three endpoints:
     - /api/v1/auth/token - generates a token for an employee when logging in with a password
     - /api/v1/all - view a list of all employees
     - /api/v1/me - view salary and date of increase by an employee by password

- [ ] .env file stores token lifetime in milliseconds and JWT secret key

- [ ] main.py - start the API. (local launch *uvicorn main:app --reload*)

- [ ] pyproject.toml - Poetry dependency file

- [ ] API files are in app folder
     - config - load environment variables
     - control - business logic functions
     - database - load database file
     - endpoints - calling API services
     - schemas - Pydentic models for variable validation

- [ ] Logins and passwords:
     | Login  | Password |
     | ------------- | ------------- |
     | Michael  | michaelsecret  |
     | Emily  | emilysecret  |

## Launch

Download files

### Running in a Docker container

*Docker and docker-compose packages must be installed*

Run the program `docker-compose up --build`

*If the python:3.10-slim image did not download automatically, first download the image `docker pull python:3.10-slim`*

Once launched, the API is available at `http://localhost:8000/docs`

### Local launch

The application has been tested on Linux Debian 11 and Linux Ubuntu 20.04 operating systems

#### Installing dependencies with Poetry

*Installing dependencies with Poetry [instruction](https://python-poetry.org/docs/)*

If necessary, change the dependency in *pyproject.toml* on line 9 to your version of Python

Install dependencies `poetry install`

To start the virtual environment, run the command `poetry shell`

Application launch `uvicorn main:app --relaod`

Once launched, the API is available at `http://localhost:8000/docs`

#### Installing dependencies with pip

It is recommended to use a virtual environment. To activate it, run `python -m venv venv` and `source venv/bin/activate`

Install dependencies in the virtual environment `pip install fastapi httpx passlib pytest_asyncio python-dotenv python-jose python-multipart pytest uvicorn`

You may need to restart the virtual environment `deactivate && source venv/bin/activate`

Application launch `uvicorn main:app --relaod`

Once launched, the API is available at `http://localhost:8000/docs`

## Testing

The configuration file and the test file are located in the 'tests' folder.

### Running in a docker container

*Docker and docker-compose packages must be installed*

Run command `docker-compose -f docker-compose.tests.yml up --build`

### Locally

Install dependencies as mentioned in **Local launch**

Run tests `pytest`

