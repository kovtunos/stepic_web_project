import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/box/web/ask')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")

application = get_wsgi_application()
