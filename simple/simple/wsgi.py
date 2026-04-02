"""
WSGI config for simple project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO celes 260402 : EC2의 경우 settings.production.py를 사용하도록 설정
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple.settings.production')

application = get_wsgi_application()
