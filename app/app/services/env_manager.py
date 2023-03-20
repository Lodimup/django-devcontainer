"""
This module is responsilbe for making sure that all the environment variables are set.
"""
import os

load_envs = [
    'DJ_POSTGRES_USER',
    'DJ_POSTGRES_PASSWORD',
    'DJ_POSTGRES_HOST',
    'DJ_POSTGRES_PORT',
    'DJ_POSTGRES_DB',

    'DJ_CELERY_BROKER_URL',
    'DJ_CELERY_RESULT_BACKEND',

    'DJ_REDIS_CACHE_URL',
]

env = {}

try:
    for i in load_envs:
        env[i] = os.environ[i]
except KeyError as e:
    raise Exception(f'Environment variable {e} is not set')
