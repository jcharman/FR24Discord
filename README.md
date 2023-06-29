# FR24Discord

Python script to collect tracked flights and send these to a Discord channel

## Usage

A Dockerfile is provided to run under Docker

1. Clone the reposiotory
```
$ git clone https://github.com/jcharman/FR24Discord
$ cd FR24Discord
```

2. Edit fr24discord.conf

3. Build and run the Docker container
```
$ docker build -t fr24discord .
$ docker run -d --restart unless-stopped fr24discord 
```
