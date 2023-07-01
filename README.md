# FR24Discord

Python script to collect tracked flights and send these to a Discord channel

## Usage

A Dockerfile is provided to run under Docker. This can either be built locally or pulled from Docker Hub.

### Pull from Docker Hub

```
$ docker pull jakecharmanuk/fr24discord:latest
$ docker run -e FR24_HOST=192.168.1.4 -e DISCORD_WEBHOOK=ZXZlcnl0aGluZ21vZGVsYWN0dWFsbHlkYW5jZWFyb3VuZGZpcmVwbGFjZXNjcmVlbm0-d --restart unless-stopped jakecharmanuk/fr24discord
```

### Build locally

1. Clone the reposiotory
```
$ git clone https://github.com/jcharman/FR24Discord
$ cd FR24Discord
```

2. Build and run the Docker container
```
$ docker build -t fr24discord .
$ docker run -e FR24_HOST=192.168.1.4 -e DISCORD_WEBHOOK=ZXZlcnl0aGluZ21vZGVsYWN0dWFsbHlkYW5jZWFyb3VuZGZpcmVwbGFjZXNjcmVlbm0-d --restart unless-stopped fr24discord 
```

## Supported environment variables

| Variable | Description
|---|---|
| FR24_HOST | Hostname or IP where dump1090 is running |
| DUMP1090_PORT | Port of dump1090 (Optional, default 80) |
| DISCORD_WEBHOOK | Last part of the Discord webhook URL |
| FR24_DELAY | Delay between requests to dump1090 in seconds (Optional, default 60)
