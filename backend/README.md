


### Use `fixture_db_data.json` to load data to DB.
- but all models are without images (later Oleh Oryshchuk will fix it)
- there are 24 users (12 men and 12 woman) and 25 is admin user
- first run the command `python manage.py migrate` and then
- use `python manage.py loaddata seed_data\fixture_db_data.json` to load data to DB.
- run command `python manage.py runserver`
- 25 user is admin with password `rvt3456`, fullname `Main Admin`, email `testadmin@gmail.com`
- Use above credentials in `http://127.0.0.1:8000/admin`

### Custom commands during development and staging
- Additionally, we can use custom commands:
  - `python manage.py model_db --num_entries 100` - creates 100 models and writes to DB
  - `python manage.py model_db --num_entries 100 --model_image` - creates 100 models with images and writes to DB
  - `python manage.py user_db --num_entries 100` - creates 100 users writes to DB
  - `python manage.py newsletter_db --num_entries 100` - creates 100 newsletters and writes to DB
  - `python manage.py newsletter_db --num_entries 100 --newsletter_image` - creates 100 newsletters with images and writes to DB
