import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgreslq_psycopg2',
        'NAME': 'db',
        'USER': 'postgre',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': 5432
    }
}