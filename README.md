# EC-Commerce

## Setup

The first thing to do is to clone the repository:
```sh
$ https://github.com/Cstephen13/backend-ecommerce.git
$ cd backend-ecommerce/backend_e_commerce
```
Create a virtual environment to install dependencies in and activate it:
```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies run the command to generate the migrations in database:

```sh
(env)$ cd backend_e_commerce
(env)$ python manage.py makemigrations
```
Once `makemigrations has finished run the migrations command:
```sh
(env)$ python manage.py migrate
```

Once `migrate` has finished run the server:
```sh
(env)$ python manage.py runserver
```
