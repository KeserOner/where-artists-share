import os

from was.settings.base import *

DATABASES['default']['NAME'] = 'was_db_test'
DATABASES['default']['USER'] = 'was'
DATABASES['default']['PASSWORD'] = os.environ.get('DB_TEST_PASSWORD', '')
DATABASES['default']['HOST'] = '127.0.0.1'
DATABASES['default']['PORT'] = '5432'
