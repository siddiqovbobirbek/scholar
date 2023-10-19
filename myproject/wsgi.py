"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

# from importlib import reload
import os

os.environ['LANG']='en_US.UTF-8'
os.environ['LC_ALL']='en_US.UTF-8'
import sys
# reload(sys)
sys.setdefaultencoding('utf-8')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
