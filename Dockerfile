FROM ubuntu:latest

MAINTAINER Abdemanaaf Ghadiali <abdemanaafzghadiali@gmail.com>

RUN apt update
RUN apt upgrade -y

RUN apt install vim -y

RUN apt install -y python3.6 python3-pip python3-dev build-essential gcc \
    libsnmp-dev snmp-mibs-downloader

RUN pip3 install --upgrade pip

RUN pip install pycrypto
RUN pip install django
RUN pip install gunicorn

RUN mkdir /app
COPY . /app
WORKDIR /app

EXPOSE 8000
#CMD exec gunicorn Capstone_Project_Django.wsgi:application --bind 0.0.0.0:8000 --workers 3

RUN /bin/bash
