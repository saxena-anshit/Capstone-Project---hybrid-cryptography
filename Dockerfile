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

COPY User_Input.py /app/User_Input.py
COPY Decrypt_File.py /app/Decrypt_File.py
COPY Encrypt_File.py /app/Encrypt_File.py

COPY /Utilities/RSA_Encryption.py /app/Utilities/RSA_Encryption.py
COPY /Utilities/Hash_Algorithm.py /app/Utilities/Hash_Algorithm.py
COPY /Utilities/One_Time_Pad.py /app/Utilities/One_Time_Pad.py

RUN /bin/bash
