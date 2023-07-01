#!/usr/bin/python3

from requests import get, post
from sys import stderr
from time import sleep
from os import environ

# Get the flights from an instance of dump1090
def getFlights(host, port):
    endpoint = f'http://{host}:{port}/dump1090/data/aircraft.json'
    flights = get(endpoint).json()
    return flights['aircraft']

# Check if a flight is one of the last 100 we sent since we started. 
def checkDupe(flight):
    if flight in sentFlights:
        return True
    else:
        sentFlights.append(flight)
        while len(sentFlights) > 100:
            del sentFlights[0]

# Send a flight number to Discord.
def sendToDiscord(flight, webhook):
    try:
        flightNum = flight['flight']
    except KeyError:
        return

    if flightNum != '' and not checkDupe(flightNum):
        message = f'New flight seen!\n[{flightNum}](https://flightradar24.com/{flightNum})' 
        try: 
           post(f'https://discord.com/api/webhooks/{webhook}', json={'content':message})
        except:
            pass

# Exit with an error message.
def exitErr(message, code):
    print(message, file=stderr)
    exit(code)

def warn(message):
    print(message, file=stderr)

# Read in the config file.
def readConfig():
    # Read in config from environment variables.
    try:
        host = environ['FR24_HOST']
    except KeyError:
        exitErr('Required environment variable not set: FR24_HOST', 1)
    try:
        port = environ['DUMP1090_PORT']
    except KeyError:
        warn('Environment variable DUMP1090_PORT not set. Using default: 80')
        port = '80'
    try:    
        webhook = environ['DISCORD_WEBHOOK']
    except KeyError:
        exitErr('Required environment variable not set: DISCORD_WEBHOOK', 1)
    try:
        delay = environ['FR24_DELAY']
    except KeyError:
        warn('Environment variable FR24_DELAY not set. Using default: 60')
        delay = 60

    # Return the config as a dict if we managed to populate all the configs.
    try:
        return({'host':host,'port':port,'webhook':webhook,'delay':delay})
    except UnboundLocalError:
        exitErr('Missing required configuration', 1)

def main():
    config = readConfig()
    while True:
        sleep(int(config['delay']))
        flights = getFlights(config['host'], config['port'])
        for flight in flights:
            sendToDiscord(flight, config['webhook'])

if __name__=='__main__':
    sentFlights = []
    main()
