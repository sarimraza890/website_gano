# Gano Endodontics Website

Two-page Django website built from the provided Figma references.

## Pages

- `/` Meet the Doc
- `/services/` Our Services and contact form

## Setup

> Use Python 3.12 or 3.13 for this project. Django 5.1.6 is not compatible with Python 3.14.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Cloud Database

Set `DATABASE_URL` to a hosted Postgres connection string before running migrations in production.

```bash
DATABASE_URL=postgresql://user:password@host:5432/database
python manage.py migrate
```

Contact form submissions are stored in the `ContactEntry` model and can be viewed in Django admin.
