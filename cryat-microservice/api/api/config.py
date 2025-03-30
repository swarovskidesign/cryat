import json
from os import environ
import environ


env = environ.Env()
env.read_env(".env")


# SYSTEM
DEBUG = env.bool("DEBUG", default=True)
SECRET_KEY = env("SECRET_KEY", default="django-insecure-&#*r2the23dm*-r+)w57)&u_%^!s+np-(%))$o(gbpg*4_!9uv")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# KAFKA
KAFKA_HOST = env("KAFKA_HOST", default="localhost")
KAFKA_PORT_BROKER = env.list("KAFKA_PORT_BROKER", default=[])
KAFKA_PORT_CONTROLLER = env.list("KAFKA_PORT_CONTROLLER", default=[])

# MICROSERVICE
MICROSERVICE_STR = env("MICROSERVICE", default='{}')
try:
    MICROSERVICE = json.loads(MICROSERVICE_STR)
except json.JSONDecodeError:
    MICROSERVICE = {}

# Другие настройки, если необходимо
# ...

# Отладочный вывод (полезно для проверки)
# print(f"DEBUG: {DEBUG}")
# print(f"SECRET_KEY: {SECRET_KEY}")
# print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
# print(f"KAFKA_HOST: {KAFKA_HOST}")
# print(f"KAFKA_PORT_BROKER: {KAFKA_PORT_BROKER}")
# print(f"KAFKA_PORT_CONTROLLER: {KAFKA_PORT_CONTROLLER}")
# print(f"MICROSERVICE: {MICROSERVICE}")