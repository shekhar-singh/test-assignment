# Test-assignment

## Objective
Design and implement a Django application with User and ActivityPeriod models,
Write a custom management command to populate the database with some dummy data,
Design an API to serve that data in the json format

## To run locally, do the usual:

Clone the project

Create a Python 3.6 virtualenv

Install dependencies:

    pip install -r requirements.txt
  
Make migrations

    python manage.py makemigrations
  
    python manage.py migrate
  
    python manage.py runserver
  
Custom management command

    python manage.py fakedataset 5
 
 5 fakedataset created succesfully
 
 ##Endpoint

local : http://127.0.0.1:8000/api/

live : http://18.219.45.199/api/
