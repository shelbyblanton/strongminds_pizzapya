# PizzaPya Pizza Manager App

## Introduction

The goal of the PizzaPya Manager App project is to provide a Django Pizza project starter template that everyone can use. This template works out of the box and can expanded upon in many different ways.

This application is written with Django 4.2.4 and Python 3.11.

![alt text](https://pizzapya.s3.us-west-1.amazonaws.com/pizzapya-screenshot.png)

### Main Features
The home page displays a list of pizzas and toppings, as well as select details about each. 
Pizza items displays:
- Image
- Name
- Cost
- Toppings List

Topping items displays:
- Image
- Name
- Cost
- Category

Each pizza and topping listed on the homepage links through to a detail page about that particular item as shown here:

![alt_text](https://pizzapya.s3.us-west-1.amazonaws.com/pizzapya-pizza-detail.png)
![alt_text](https://pizzapya.s3.us-west-1.amazonaws.com/pizzapya-topping-detail.png)

### Pizza and Topping Management done via Django Admin Portal
![alt text](https://pizzapya.s3.us-west-1.amazonaws.com/pizzapya-admin.png)

All CRUD operations are fulfilled in Django's Admin system. To access, click on the `Admin Console` link in the footer, or navigate to `/admin`.

## Usage & Requirements

To use this template to start your own project:

### Existing virtualenv
If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django

And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.


# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/strongminds_pizzapya.git
    $ cd strongminds_pizzapya
    
Then activate the `virtualenv` for your project.
    
We now need to install project dependencies:

    $ pip install -r requirements/local.txt

This project requires a `.env` file to operate, so next create an `.env` file in the `strongminds_pizzapya` directory with the keys for the following variables without quotation marks ( *these may have been emailed to you* ):

    SECRET_KEY=
    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    DATABASE_NAME=
    DATABASE_USER=
    DATABASE_PASS=

Now onto data. To set up the database tables, we need to apply the migrations:

    $ python manage.py migrate

And then load the initial data:

    $ python manage.py loaddata initial_data

**Setup is complete!** 

Now we start the development server:

    $ python manage.py runserver

and point our browser to `http://127.0.0.1:8000/` to see the app in action.

# Testing

As this is a stripped-down starter template, there are only 4 tests that need to be run.

To run these tests, type the following into the Python terminal:
    
    $ python manage.py test


# Author & Credits

Written by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)**.

Starter pizza and topping images courtesy of **[Adobe Stock](https://stock.adobe.com/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aimage%5D=1&k=vegetables+isolated&order=relevance&safe_search=1&limit=100&search_page=1&search_type=usertyped&acp=&aco=vegetables+isolated&get_facets=0)** previews. 

