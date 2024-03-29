from ibuy.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-c403d.up.railway.app']  
#ALLOWED_HOSTS = ['127.0.0.1']  

