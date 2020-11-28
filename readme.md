### Create virtual enviroment

- > python3 -m venv myvenv

### Activate virtual enviroment

- > . myvenv/Scripts/activate

### Install requirements

- > pip install -r requirements.txt

### Enter project folder

- > cd danielle

### Makemigrations and migrate

- > python manage.py makemigrations
- > python manage.py migrate

### Create superuser

- > python manage.py createsuperuser

### Run seeds

- > python manage.py loaddata seed/people.json

### Test (for while, it's hand make)