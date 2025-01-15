
### Use `fixture_db_data.json` to load data to DB.
- but all models are without images (later Oleh Oryshchuk will fix it)
- there are 24 users (12 men and 12 woman) and 25 is admin user
- first run the command `python manage.py migrate` and then
- use `python manage.py loaddata seed_data\fixture_db_data.json` to load data to DB.
- run command `python manage.py runserver`
- 25 user is admin with password `rvt3456`, name `Main`, username `Admin`, email `testadmin@gmail.com`
- Use above credentials in `http://127.0.0.1:8000/admin`
