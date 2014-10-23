# Lomakekala - Generic form generator

## Getting started

    virtualenv venv-lomakekala
    source venv-lomakekala/bin/activate

    git clone https://github.com/japsu/lomakekala
    cd lomakekala
    pip install -r requirements.txt

    python manage.py migrate
    python manage.py setup_lomakekala_test_app
    python manage.py runserver

    open http://localhost:8000/test
    open http://localhost:8000/admin/

`setup_lomakekala_test_app` created a user called `mahti` with password `mahti`.
