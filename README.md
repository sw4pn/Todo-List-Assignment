# Todo-List-Assignment
 Todo-List-Assignment: Python, Django Backend, Django Rest Framerwork, Rest API
 
# Description
To-Do Application developed with Django Rest Framework.

* Basic Authentication Enabled:
   - username: **admin**
   - password: **123456**

 * Test this LIVE at:
   
   - Admin Section:  `https://sw4pn.pythonanywhere.com/admin/`
   
   - API URL :  `https://sw4pn.pythonanywhere.com/api/`

## End Points for Task

* CREATE a todo item   * `POST /api/tasks/`
* READ all todo items  * `GET /api/tasks/`
* READ one todo item   * `GET /api/tasks/{pk}/`
* UPDATE a todo item   * `PATCH /api/tasks/{pk}/`
* DELETE a todo item   * `DELETE /api/tasks/{pk}/`

## End Points for Tags

* CREATE a tag   * `POST /api/tags/`
* READ all tags  * `GET /api/tags/`
* READ one tag   * `GET /api/tags/{pk}/`
* UPDATE a tag   * `PATCH /api/tags/{pk}/`
* DELETE a tag   * `DELETE /api/tags/{pk}/`

## Get the code

* Clone the repository
`git clone https://github.com/sw4pn/Todo-List-Assignment.git`


## Install the project dependencies

* First create virtualenv
  - install virutal environment:
    `pip install virtualenv`
    
  - test installation:
    `virtualenv --version`
    
  - create virtual environment:
    `virtualenv todo-env`

  - start virtual environment:
    `todo-env\Scripts\activate`

* Install dependencies

  - move to project dir:
    `cd Todo-List-Assignment`
    
  - enter the following command.
    `pip install -r requirements.txt`

## Run the commands to generate the database

`python manage.py makemigrations`

`python manage.py migrate`

## Generate super user

`python manage.py createsuperuser`

## Run the server

`python manage.py runserver` 

the application will be running on port 8000 **http://127.0.0.1:8000/**
the admin section can be accessed from **http://127.0.0.1:8000/**
