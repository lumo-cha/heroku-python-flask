# Barebones Heroku Flask App
This repo contains the minimum required files to start building a Flask app on Heroku.

## Required Software
+ heroku toolbelt: [Download Here](https://toolbelt.heroku.com/)
+ Python 3
+ virtualenv, pip

## Initial Setup
All work should be done in a virtual environment locally.<br>
```python
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running and Testing the App Locally
The heroku toolbelt provides the necessary tools to run and test endpoints from
your local machine. [More Info](https://devcenter.heroku.com/articles/heroku-local#run-your-app-locally-using-the-heroku-local-command-line-tool)<br>
```heroku local web -f Procfile_local -e .env```

End the virtual environment:<br>
```deactivate```

## Test Endpoints
1. ```/hello``` -- this endpoint returns the string "hello world". the app, at its most basic
level, works if this endpoint works.
2. ```/config``` -- returns a json string containing all the config variables set in flask
