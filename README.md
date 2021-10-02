# AutomaTik Installation

AutomaTik is an automation system for MikroTik devices with simplicity and security in mind. Winbox is the main tool for MikroTik management, but it can be overwhelming for beginners. AutomaTik will help you configure your MikroTik device easily.


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
docker-compose up -d
```

## [InfluxDB Configuration](docs/influx_config.md)


## [Minio Configuration](doc/minio_config.md)


