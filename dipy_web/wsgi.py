"""
WSGI config for dipy_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# imports for heroku
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dipy_web.settings")

application = get_wsgi_application()

# additional steps for heroku
application = DjangoWhiteNoise(application)
