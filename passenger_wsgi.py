import os, sys

# Add the project root
sys.path.insert(0, "/home/nmimsindore/ACM-Django")

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acm_django.settings")

# Load application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
