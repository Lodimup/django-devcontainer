"""
This module is responsilbe for making sure that all the environment variables are set.
"""
import os

try:
    DJ_POSTGRES_USER = os.environ['DJ_POSTGRES_USER']
    DJ_POSTGRES_PASSWORD = os.environ['DJ_POSTGRES_PASSWORD']
    DJ_POSTGRES_HOST = os.environ['DJ_POSTGRES_HOST']
    DJ_POSTGRES_PORT = os.environ['DJ_POSTGRES_PORT']
    DJ_POSTGRES_DB = os.environ['DJ_POSTGRES_DB']

    DJ_CELERY_BROKER_URL = os.environ['DJ_CELERY_BROKER_URL']
    DJ_CELERY_RESULT_BACKEND = os.environ['DJ_CELERY_RESULT_BACKEND']

    DJ_REDIS_CACHE_URL = os.environ['DJ_REDIS_CACHE_URL']
except KeyError as e:
    raise Exception(f'Environment variable {e} is not set')

env = {
    'DJ_POSTGRES_USER': DJ_POSTGRES_USER,
    'DJ_POSTGRES_PASSWORD': DJ_POSTGRES_PASSWORD,
    'DJ_POSTGRES_HOST': DJ_POSTGRES_HOST,
    'DJ_POSTGRES_PORT': DJ_POSTGRES_PORT,
    'DJ_POSTGRES_DB': DJ_POSTGRES_DB,

    'DJ_CELERY_BROKER_URL': DJ_CELERY_BROKER_URL,
    'DJ_CELERY_RESULT_BACKEND': DJ_CELERY_RESULT_BACKEND,

    'DJ_REDIS_CACHE_URL': DJ_REDIS_CACHE_URL,
}
