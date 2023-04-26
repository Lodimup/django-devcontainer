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

    'DJ_DEBUG',
    'DJ_SECRET_KEY',
]

env = {}
envs_notset = []

for i in load_envs:
    try:
        env[i] = os.environ[i]
    except KeyError as e:
        if os.getenv('SKIP_ENV_CHECK').lower() == 'true':
            print(f"WARNING: Environment variable {i} not set")
        else:
            envs_notset.append(i)

if len(envs_notset) > 0:
    raise Exception(f"Environment variables not set: {envs_notset}")

# Typecasts
if hasattr(env, 'DJ_DEBUG'):
    env['DJ_DEBUG'] = env['DJ_DEBUG'].lower() == 'true'
