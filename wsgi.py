import os
import sys
from django.core.wsgi import get_wsgi_application

# This line helps the server find your settings inside the folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'showshelf_project.settings')

application = get_wsgi_application()
