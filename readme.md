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

- > python manage.py runserver

## Steps done

### Models
- Create people app
- Add People app in settings
- Create the following models:
    - Base
    - Person
    - Checkin
    - Checkout
    - HomeServices
    - ProfessionalServices
- Add verbose name to models
- Add help text to models
- Add `__str__` to models

### Admin
- Register model to admin
- Customize section fields
- Customize list display
- Customize list filter
- Customize search fields
- Customize inline fields
- Customize collapse section fields

### Settings
- Add Authentication
- Add Permission
- Add Time Zone
- Add Language

## Formatters and validations

- Create format numerical string inputs
- Create format string inputs
- For each field in models, create a format, if necessary
- For each field in models, create a validation, if necessary
- Create unit test for all formatters and validations above

### Serializers