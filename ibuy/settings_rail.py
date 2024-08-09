from ibuy.settings import *
from decouple import config
# Security settings
SECRET_KEY = config('SECRET_KEY')

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode': 'disable'},  # Add sslmode if required
    }
}


ALLOWED_HOSTS = ['https://django-rail-production-f714.up.railway.app/']

