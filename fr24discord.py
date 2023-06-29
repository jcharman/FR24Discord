#!/usr/bin/python3

from requests import get, post
from sys import stderr
from time import sleep

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

    if flightNum != "" and not checkDupe(flightNum):
        message = f'New flight seen!\n[{flightNum}](https://flightradar24.com/{flightNum})' 
        try: 
           post(f'https://discord.com/api/webhooks/{webhook}', json={'content':message})
        except:
            pass

# Exit with an error message.
def exitErr(message, code):
    print(message, file=stderr)
    exit(code)

# Read in the config file.
def readConfig(configPath):
    # Read in parameters from the config file.
    try:
        configFile = open(configPath, 'r')
    except FileNotFoundError:
        print("Configuration file does not exist.")
        exit(1)

    # Read in all lines except those starting with a # or a non-alphanumeric char.
    configLines = configFile.readlines()
    for line in configLines:
        if line[0] == "#":
            continue
        if not line[0].isalnum():
            continue

        # Remove any spaces from the line then split it to an array on the = sign.
        splitLn = line.replace(" ", "").strip().split('#')[0].split("=")

        # Pull in the known config lines.
        if (splitLn[0] == "fr24host"):
            host = splitLn[1]
        elif (splitLn[0] == "dump1090port"):
            port = splitLn[1]
        elif (splitLn[0] == "discordwebhook"):
            webhook = splitLn[1]
        elif (splitLn[0] == "delay"):
            delay = int(splitLn[1])
        else:
            # Error out on an unknown config line.
            exitErr(f'Unknown config: {splitLn[0]}', 1)
    
    # Return the config as a dict if we managed to populate all the configs.
    try:
        return({'host':host,'port':port,'webhook':webhook,'delay':delay})
    except UnboundLocalError:
        exitErr('Missing required configuration', 1)

def main():
    config = readConfig('/etc/fr24discord/fr24discord.conf')
    while True:
        sleep(config['delay'])
        flights = getFlights(config['host'], config['port'])
        for flight in flights:
            sendToDiscord(flight, config['webhook'])

if __name__=='__main__':
    sentFlights = []
    main()
