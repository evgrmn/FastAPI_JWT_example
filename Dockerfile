FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./pyproject.toml .
RUN pip install "poetry==1.5.0"
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .
