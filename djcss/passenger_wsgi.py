import os
import sys

# Path to your Django project directory
project_home = '/home/drjohnch/djcss'

# Add your project to the system path
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable for Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'djcss.settings'

# WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
