"""
WSGI config for capstone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the system path
sys.path.append('/home/om-pujari/capstone')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')

# Activate the virtual environment (if using one)
activate_env = '/home/om-pujari/.virtualenvs/yourvenv/bin/activate_this.py'
if os.path.exists(activate_env):
    with open(activate_env) as f:
        exec(f.read(), dict(__file__=activate_env))

# Import and run the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

