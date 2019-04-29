FROM python:latest

MAINTAINER Abdemanaaf Ghadiali <abdemanaafzghadiali@gmail.com>

ENV PYTHONUNBUFFERED 1

RUN pip install pycrypto
RUN pip install django
RUN pip install django-crispy-forms

RUN mkdir /project
WORKDIR /project
COPY . /project/