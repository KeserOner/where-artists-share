from .base_settings import *

DEBUG = True

DATABASES['default']['NAME'] = 'was'
DATABASES['default']['USER'] = 'was'
DATABASES['default']['PASSWORD'] = 'foobar'
DATABASES['default']['HOST'] = 'db'
DATABASES['default']['PORT'] = '5432'

ALLOWED_HOSTS = ['*']
