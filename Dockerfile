FROM python:3.11-alpine

RUN mkdir -p /opt/fr24discord

COPY ./fr24discord.py /opt/fr24discord/fr24discord.py

RUN pip3 install requests

ENTRYPOINT [ "python3", "/opt/fr24discord/fr24discord.py" ]
