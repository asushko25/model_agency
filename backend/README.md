## Model Agency web-application

![Django](https://img.shields.io/badge/Django-5.1.4-brightgreen.svg)
![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-3.15.2-blue.svg)

Model Agency is a web application powered by Django REST Framework, designed to connect you with the perfect
model for your creative projects. Whether you need assistance from a professional agency for in-depth research
or prefer to explore independently, the platform provides advanced filtering and search tools to help you find
the ideal match effortlessly.

## Features
* Superuser (admin, staff) have admin site http://localhost:8000/admin/ with full control
    and with full control on platform.
* There is also different feature like searching/filtering lists of data
    which you can see on api docs
* Caching using Redis during production and staging, but for development we are using dummy.
* Using most popular and well-supported DB PostgresSQL.
* Project cover with tests using Djagno/DRF build-in support and Locust tests to discover bottlenecks of application
* API documentation  http://127.0.0.1:8000/api/doc/swagger/

## Installation
1. Clone git repository to your local machine:
```
    https://github.com/OlehOryshchuk/model_agency.git
```
2. Create virtual environment `python -m venv venv`, then activate it:
  - On Windows (CMD / PowerShell) `venv\Scripts\activate` or on Powershell `venv\Scripts\Activate.ps1`
  - macOS / Linux (Bash / Zsh) `source venv/bin/activate` or `source venv/Scripts/activate`

3. Install Dependencies `pip install -r requirements.txt`

4. Copy the `.env.sample` file to `.env` and configure the environment variables. But for local development
    you need to declare only `DJANGO_ENV=development`, `DJANGO_SECRET_KEY=...` and `DJANGO_SETTINGS_MODULE=model_agency.settings`.
   To copy on Windows CMD use `copy .env.sample .env`, Windows PowerShell `Copy-Item .env.sample -Destination .env`,
   Windows (Git Bash, WSL)/Linux/macOS - `cp .env.sample .env`

5. Apply Migrations:
   - `python manage.py makemigrations` - create migrations
   - `python manage.py migrate` - run migrations
   - `python manage.py createsuperuser`- Create a superuser (optional, for admin access):
6. Optional, you can load small data - `python manage.py loaddata seed_data/fixture_db_data.json`
   it also loads admin user specified below

7. Access API as superuser you can use the following admin user account:
   - **Email**`testadmin@gmail.com` : Email is not valid
   - **Password** `rvt3456`
   - **Username** `Main Admin`
   - Or you can create your own using `python manage.py createsuperuser`

8. Run Tests (Optional) - `python manage.py test`
9. Run web application locally `python manage.py runserver`

### Usage
To access the API, navigate to http://localhost:8000/api/ in your web browser and enter one of endpoints.

### Custom commands during development and staging
- Additionally, we can use custom commands, but only when `DJANGO_ENV` is `development` or `staging`:
  - `python manage.py model_db --num_entries 100` - creates 100 models and writes to DB
  - `python manage.py model_db --num_entries 100 --model_image` - creates 100 models with images and writes to DB
  - `python manage.py user_db --num_entries 100` - creates 100 users writes to DB

### Testing application using Locust.
- We can test application using Locust, which allows to mimic real user traffic, finding bottlenecks, testing
  performance of our application.
  - Run Locust tests using Docker `docker-compose -f locust_tests/docker-compose.yml up --build -d`
    - Creates 1 Master and 1 Worker - which executes tests.
    - We can make more Workers by using `--scale worker=4` in 
      `docker-compose -f locust_tests/docker-compose.yml up --build --scale worker=4 -d`
    - Each worker is a separate process. If you have 4 CPUs and run 10 workers, they may compete for resources,
      which can affect performance. Usually, 1-2 workers per CPU core is recommended, but it depends on the type of test.
  - After Docker Locust is running you can enter `http://localhost:8089/` if testing locally.
  - To stop Docker containers use `docker-compose -f locust_tests/docker-compose.yml down`
