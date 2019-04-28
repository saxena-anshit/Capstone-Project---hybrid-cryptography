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

RUN mkdir /app

COPY . /app

RUN /bin/bash
