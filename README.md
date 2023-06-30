# FR24Discord

Python script to collect tracked flights and send these to a Discord channel

## Usage

A Dockerfile is provided to run under Docker

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
