### Create virtual enviroment

- > python -m venv myvenv

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

### Test and coverage

- > pytest
- > coverage run -m pytest
- > coverage html

### Run the application

- > python manage.py runserver

### Rotas

- Users
    - `POST /users/` -> Create new user (username,password,email)
    - `POST /login/` -> Create token (username,password)
- People
    - `GET /api/v1/people/` -> List all people.
    - `POST /api/v1/people/` -> Create new person.
    - `GET /api/v1/people/<int:id>/` -> List person by id.
    - `PUT /api/v1/people/<int:id>/` -> Replace all mandatory fields. plus fields in request.
    - `Patch /api/v1/people/<int:id>/` -> Replace only fields in request.
    - `Delete /api/v1/people/<int:id>/` -> Delete person by ID


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
- Add blank and null, if necessary
- Add `__str__` to models
- Add validators (CPF, CEP, EMAIL, ...)
- Add formatted_field methods to after deserialization

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
- Add Cors
- Add Pagination

## Validations

- For each field in models, create custom validations, if necessary
- Create unit test for all validations above

### Serializers

- Exclude fields if necessary
- 

### Views

- Add class methods (choose right)
- Add filters
- Add search
- Add authentications, authorization, permissions


- **TODO**