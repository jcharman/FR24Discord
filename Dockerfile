FROM python:3.11-alpine

RUN mkdir -p /opt/fr24discord
RUN mkdir -p /etc/fr24discord

COPY ./fr24discord.py /opt/fr24discord/fr24discord.py
COPY ./fr24discord.conf /etc/fr24discord/fr24discord.conf

RUN pip3 install requests

ENTRYPOINT [ "python3", "/opt/fr24discord/fr24discord.py" ]
