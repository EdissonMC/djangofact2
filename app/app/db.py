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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbvtpmvtdfj52g',
        'USER': 'qdxgvrgqojvjxc',
        'PASSWORD': '87364a161052388d120cb28fcd835d0d9e1bfaa98d18089186afe3ecee357cb5',
        'HOST': 'ec2-52-3-4-232.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

