FROM python:3.7.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /api

WORKDIR /api

COPY . .

RUN pip install -r requirements.txt