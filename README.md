## Project Name:
Awwards

### Author
Jacob Rugano

### Description
This application allows a user to post a project he/she has created and get it reviewed by his/her peers based on design, usability and content.

### User Story
A user of the application is able to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View their profile page
7. Getting Started
8. To set up the project in your local machine for development and testing:

### Clone this Repository
git clone https://github.com/jacobrugano/projectsdjangoip3.git

#### Enable your Python development environment Add Python, pip and a virtual environment to get started:
1. $ python3.6 -m venv --without-pip virtual

2. $ source virtual/bin/activate

3. (virtual) $ curl https://bootstrap.pypa.io/get-pip.py | python

#### Prerequisites
Install all project requirements using the package manager pip.

(virtual) $ pip install -r requirements.txt

Installation
Use the .env.example file to create a .env file with appropriate values to get a development env running.

Create a postgres db and add the credentials to .env file

Apply initial migrations

(virtual) $ python manage.py migrate

Create admin account

(virtual) $ python manage.py createsuperuser

Make migrations to your database

(virtual) $ python manage.py makemigrations (app name)

(virtual) $ python manage.py migrate

Start development server

(virtual) $ python3 manage.py runserver

#### Running Tests
To run automated tests for the system:

(virtual) $ python3 manage.py test (app name)

### Deployment
With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live or simply run it locally

(virtual) $ python3 manage.py runserver

#### Technology Used
1. Django 3.0.8 - The web framework used
2. Heroku - Deployment platform
3. Python3 - Backend logic
4. Postresql - Database system

### Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

#### Contact Information
If you have any question or contributions, please email: jerushaotienocoding@gmail.com

### License
MIT License

### Copyright
Copyright (c) 2022 Jacob Rugano