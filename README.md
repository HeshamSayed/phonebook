# phonebook

The Phonebook Application is a simple Django-based web application designed to manage contacts effectively. This application provides a convenient platform for users to store and retrieve their contact information with ease.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Prerequisites
Before you begin, ensure you have met the following requirements:

You have installed Docker and Docker Compose.
You have a basic understanding of Docker and Django.


# Using Phonebook Django Application
    $ git clone https://github.com/your-repo-link/phonebook.gitz


# Navigate to the project root directory:

    $ cd phonebook

# Build and run the Docker containers:

    $ docker-compose up --build

# To stop and remove containers, networks and volumes, you can use:
    
    $ docker-compose down

# To access the application, open your web browser and navigate to:

    $ http://localhost:8000/


# Database schema

    Contact Table:

        Field	Type	Constraints
        id	Integer	Primary Key, Auto Increment
        user_id	Integer	Foreign Key (references User(id)), Not Null
        firstname	Varchar(100)	Not Null
        lastname	Varchar(100)	Not Null
        email	Varchar(100)	Not Null

The Contact table has a foreign key user_id referencing id in the User table (which is Django's built-in User model, typically stored in a table named auth_user). This establishes a many-to-one relationship from Contact to User, meaning each contact is associated with one user, and each user can have multiple contacts.

    PhoneNumber Table:

        Field	Type	Constraints
        id	Integer	Primary Key, Auto Increment
        contact_id	Integer	Foreign Key (references Contact(id)), Not Null
        mobile_phone	Varchar(100)	Not Null

The PhoneNumber table has a foreign key contact_id referencing id in the Contact table. This establishes a many-to-one relationship from PhoneNumber to Contact, meaning each phone number is associated with one contact, and each contact can have multiple phone numbers.


# ENV VARIABLES
    DO not forgot to add the credentials for the database 
    we used here postgres

    credentails will be added in .env file as the following create your own one as we do not push this file to git
    Example :
        DB_NAME=phonebook
        DB_USER=postgres
        DB_PASSWORD=password
        DB_HOST=localhost
        DB_PORT=5432


## Endpoints


    POST /add/: Add a new contact. The request body should include firstname (string), lastname (string), email (string), and optionally phone_numbers (list of strings). This corresponds to the AddContactView.
    
    GET /list/: Retrieve a list of all contacts for the currently authenticated user. Each item in the list includes contact details and related phone numbers. This corresponds to the ContactListView.
    
    GET /int:pk/: Retrieve details of a specific contact by its ID, including related phone numbers. This corresponds to the ContactDetailView.

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.



###### App screenshots
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/login.png)
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/list.png)
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/login_succ.png)
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/form_to_add.png)
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/detail_view.png)
![alt text](https://github.com/HeshamSayed/phonebook/blob/master/screenshots/confirmation.png)
