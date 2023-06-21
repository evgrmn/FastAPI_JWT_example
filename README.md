# JWT authentication example for FastAPI with Pytest testing

## What is inside

- [ ] A simple example of a REST service for viewing the current salary of company employees

- [ ] The database of company employees is located in the text file app/database/fake_users_db.json

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
     - Michael michaelsecret
     - Emily emilysecret

## Launch

Download files

### Running in a Docker container

*Docker and docker-compose packages must be installed*

Run the program `docker-compose up --build`

*If the python:3.10-slim image does not download automatically, then first download the image `docker pull python:3.10-slim`*

После запуска, API доступно по адресу `http://localhost:8000/docs`

### Локальный запуск

Работоспособность ПО проверена в операционных системах Linux Debian 11 и Linux Ubuntu 20.04

#### Установка зависимостей с помощью Poetry

*Для запуска должен быть установлен пакет Poetry [инструкция](https://python-poetry.org/docs/)*

*Если у вас установлен Python3.9 - изменить зависимость в pyproject.toml на вашу версию python*

Для установки зависимостей выполнить команду `poetry install`

Для запуска виртуального окружения выполнить команду `poetry shell`

Запустить приложение `uvicorn main:app --relaod`

После запуска, API доступно по адресу `http://localhost:8000/docs`

#### Другой способ подготовки локального запуска - это установка зависимостей с помощью pip

Рекомендуется использовать виртуальное окружение venv. Для того чтобы его активировать, выполните команду `python -m venv venv` и затем `source venv/bin/activate` 

Установить зависимости в виртуальное окружение `pip install fastapi httpx passlib pytest_asyncio python-dotenv python-jose python-multipart pytest uvicorn`

Возможно, потребуется перезапустить виртуальное окружение `deactivate && source venv/bin/activate`

Выполнить команду `uvicorn main:app --reload`

После запуска, API доступно по адресу `http://localhost:8000/docs`

## Тестирование

Файл конфигурации и файл с тестами находятся в папке tests. Тесты и комментарии к тестам в файле test_app.py

### Запуск в контейнере docker

*Для запуска должны быть установлены пакеты docker и docker-compose*

Выполнить команду `docker-compose -f docker-compose.tests.yml up --build`

### Локально

Зависимости должны быть установлены по инструкции из раздела **Локальный запуск**

Запустить тесты командой `pytest`

