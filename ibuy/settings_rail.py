from ibuy.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

#ALLOWED_HOSTS = ['web-production-b18e32.up.railway.app']  
ALLOWED_HOSTS = ['127.0.0.1']  

