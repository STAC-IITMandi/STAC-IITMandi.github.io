"""
WSGI config for web_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_main.settings")
sys.path.append('~/STAC-IITMandi.github.io/src/') # path/src
sys.path.append('~/STAC-IITMandi.github.io/src/web_main') # path/src/web_main

application = get_wsgi_application()