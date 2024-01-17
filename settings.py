# dejango-project/settings.py

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = False  # Change this to False for production

ALLOWED_HOSTS = ['dejango-project.herokuapp.com']  # Replace with your Heroku app's domain

INSTALLED_APPS = [
    'hello_world',
]

MIDDLEWARE = [
    # Add your middleware here
]

ROOT_URLCONF = 'dejango-project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dejango-project.wsgi.application'

# ... other settings ...



