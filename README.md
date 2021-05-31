# StarWars Ecommerce
`A place where you can buy anything you want to dominate the galaxy.`

* ## __About__
    - It is a funny webpage that simulate the issuing sales orders;

    - You should register, login and buy;

    - This application gives permission to buy to authenticated user, and permission to register product to superuser;

    - The authenticated user can access the product list page, and buy everything he wants;

    - The superuser can add a products to the application;

    - Whenever the superuser register a new product to the application, every registered user receive an email with news.

* ## __How to run__
  - Create a virtualenv(for unix users):
    - python3 -m venv .venv
  
  - Active the just created virtualenv:
    - source .venv/bin/activate

  - Install dependencies:
    - pip install -r requirements.txt
  
  - Config the .env file using the .env-sample file
  - Allow Third-party apps with account; access in your gmail configs;

  - Run the migrations:
    - python manage.py migrate
  
  - Run collectstatic:
    - python manage.py collecstatic

* ## __Populate Tables__
    - To create the tables automatically using django-extensions follow the steps bellow in the same order:
    
    - __Register Products:__
        - . register_products.sh
        - Once you haven't any user in your database, these process is going to be quicker than if you have registered ones.

    - __Register Users:__
        - . register_users.sh

* ## __Create the SuperUser:__
    - python manage.py createsuperuser

* ## __Run tests:__
    - pytest -v

* ## __OBS:__
    - The login must be with the email instead of username even in the admin page.
    
