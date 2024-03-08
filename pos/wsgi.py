"""
WSGI config for ems project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise
import os


from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT) 
app = application



