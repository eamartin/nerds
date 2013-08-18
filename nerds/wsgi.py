import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'nerds.settings'

import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()
