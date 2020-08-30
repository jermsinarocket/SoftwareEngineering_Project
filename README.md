# CZ2006 Software Engineering Project

# Enso 
Python version: 3.5 & above
Django version: 3.1

## Prerequisites
- Ensure VirtualEnv is Installed : `pip install virtualenv`

## Set Up
- change directory to 'SEProject': `cd SEProject`
- create a new virtual environment: `virtualenv env`
- activate the virtual environment: `env\Scripts\activate`
- update pip and setuptools to latest version: `python -m pip install --upgrade pip setuptools`
- install dependencies: `pip install -r requirements.txt`
- once done, you can deactivate the virtual environment: `env\bin\deactivate`

## Verifying Modules Installation
- To verify that Django can be seen by Python, type python from your shell. Then at the Python prompt, try to import Django:
```python
import django
django.__version__
```

## Initializing the Server
- change directory to 'tempproject': cd `tempproject`
- run the server: `python manage.py runserver`
- once done, you can deactivate the virtual environment: `env\bin\deactivate`
