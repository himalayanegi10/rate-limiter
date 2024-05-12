FROM python:3.10-bullseye

LABEL authors="himal"

RUN pip install --upgrade pip

RUN pip install -U pip setuptools poetry

WORKDIR /code

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY README.md README.md
COPY startup.sh startup.sh

RUN poetry install --no-root

EXPOSE 8000

COPY . .

RUN chmod +x startup.sh