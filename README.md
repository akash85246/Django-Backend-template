# Django Status API

Minimal Django project with a `GET /api/status/` endpoint that reports the server is online.

## Structure

```
django-project/
├── manage.py
├── requirements.txt
├── .env.example
├── backend/              # project configuration
│   ├── settings/
│   │   ├── base.py       # shared settings
│   │   ├── dev.py        # local development (default for manage.py)
│   │   └── prod.py       # production (needs env vars)
│   ├── urls.py           # root URLs, mounts app under /api/
│   ├── wsgi.py
│   └── asgi.py
└── app/                  # the application
    ├── apps.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

## Setup

```bash
conda create -n djangoenv python=3.12 -y   # or: python3 -m venv .venv
conda activate djangoenv
pip install -r requirements.txt
python manage.py runserver
```

## Try it

```bash
curl http://127.0.0.1:8000/api/status/
```

```json
{"status": "online", "message": "I am online", "timestamp": "2026-10-08T00:00:00+00:00"}
```

## Tests

```bash
python manage.py test
```

## Production

Set `DJANGO_SETTINGS_MODULE=backend.settings.prod`, `DJANGO_SECRET_KEY`, and `DJANGO_ALLOWED_HOSTS`, then serve `backend.wsgi:application` with a WSGI server such as gunicorn.
