# AutomaTik Installation

AutomaTik is an automation system for MikroTik devices with simplicity and security in mind. Winbox is the main tool for MikroTik management, but it can be overwhelming for beginners. AutomaTik will help you configure your MikroTik device easily.

[Check out AutomaTik web site for more information and documentation](https://automatik.cloud)


## Requirements
 - [Docker](https://docs.docker.com/get-docker/)
 - [Docker Compose](https://docs.docker.com/compose/)
 - Python 3.9+


## Installation
- Clone this repo. 

```
git clone https://github.com/okazdal/automatik_installation.git
```

## Create .env file
```
pip install poetry
cd automatik_installation
poetry shell
poetry install
python create_dotenv.py
```

## Start containers
```
docker-compose up -d mongo redis influxdb minio vault
```

## [InfluxDB Configuration](docs/influx_config.md)


## [Minio Configuration](docs/minio_config.md)

## Run Setup Script
```
python setup.py
```

## Start Containers
```
docker-compose up -d fastapi sio worker beat frontend
```

## Web interface

Create an entry in /etc/hosts on your computer.

```
127.0.0.1	my.automatik.cloud
```

Add 127.0.0.1 if AutomaTik is installed on same device. If you have installed AutomaTik on a server, instead of 127.0.0.1 use server IP address.

Open page [My AutomaTik Login](http://my.automatik.cloud)

![Login Page](docs/images/login.png)

