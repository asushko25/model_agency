


### Use `fixture_db_data.json` to load data to DB.
- but all models are without images (later Oleh Oryshchuk will fix it)
- there are 24 users (12 men and 12 woman) and 25 is admin user
- first run the command `python manage.py migrate` and then
- use `python manage.py loaddata seed_data/fixture_db_data.json` to load data to DB.
- run command `python manage.py runserver`
- 25 user is admin with password `rvt3456`, fullname `Main Admin`, email `testadmin@gmail.com`
- Use above credentials in `http://127.0.0.1:8000/admin`

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
  

