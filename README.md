# JWT authentication example for FastAPI with Pytest testing

REST-сервис просмотра текущей зарплаты сотрудников и даты следующего повышения. Сотрудники могут пользоваться сервисом только с помощью своего логина и пароля. Сервис информирует сотрудников об их зарплате и дате следующего повышения зарплаты. Для реализации сервиса должен быть использован FastAPI.

### Ключевые особенности

- [ ] Поскольку требования по использованию реляционных баз данных не определены, для хранения информации о сотрудниках используется простой текстовый файл в формате json

- [ ] Запуск сервиса в изолированном контейнере Docker

- [ ] Использование менеджера зависимостей Poetry

- [ ] Технология аутентификации в клиент-серверных приложениях JSON Web Token (JWT)

- [ ] Автотесты Pytest

- [ ] Программный код основан на официальной документации FastAPI [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

## Реализация

- [ ] API имеет три эндпоинта:
    - /api/v1/auth/token - генерирует токен для сотрудника при входе по паролю
    - /api/v1/all - просмотр списка всех сотрудников
    - /api/v1/me - просмотр зарплаты и даты повышения сотрудником по паролю

- [ ] файл .env хранит срок жизни токена в миллисекундах и секретный ключ JWT

- [ ] main.py - запуск API. (локальный запуск *uvicorn main:app --reload*)

- [ ] pyproject.toml - файл с зависимостями Poetry

- [ ] файлы API находятся в папке app
    - config - загрузка переменных окружения
    - control - функции бизнес-логики
    - database - загрузка файла базы данных
    - endpoints - вызов сервисов API
    - schemas - модели Pydentic для валидации переменных

- [ ] Логины и пароли:
    - Ivan ivansecret
    - Elena elenasecret

## Запуск

Скачать файлы из репозитория

### Запуск в контейнере Docker

*Для запуска должны быть установлены пакеты docker и docker-compose*

Команда запуска `docker-compose up --build`

*Если образ python:3.10-slim не скачивается автоматически, то использовать команду `docker pull python:3.10-slim`*

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
