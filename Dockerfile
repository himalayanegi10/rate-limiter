FROM python:3.10-bullseye

LABEL authors="himal"

RUN pip install --upgrade pip

RUN pip install -U pip setuptools poetry

WORKDIR /code

COPY pyproject.toml poetry.lock README.md startup.sh /code/

EXPOSE 8000

COPY . .

RUN chmod +x startup.sh