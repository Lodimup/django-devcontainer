# Django Devcontainer Base Repository
This repository contains a base devcontainer for Django development.  
It is intended to be used as a base for other repositories.  

It's already setup for the following:
- postgresql
- redis
- celery
- auto load .env.local file
- debugger
- Makefile

# Usage
clone this repository and use it as a base for your own repository.  
You will need to change the following:  
- create .env.local file at root of project
- .devcontainer/post-create.sh  
    change `django-devcontainer` to your project name
- .vscode/settings.json  
    change `django-devcontainer` to your project name, in case VSCODE does not recognize the .venv created by poetry
