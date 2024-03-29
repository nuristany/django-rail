from ibuy.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-c403d.up.railway.app']  
CSRF_TRUSTED_ORIGINS = ['https://web-production-c403d.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {
            'options': '-c search_path=public,store,core'
        }

    }
}

#ALLOWED_HOSTS = ['127.0.0.1']  

