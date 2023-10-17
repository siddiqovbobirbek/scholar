from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
<<<<<<< HEAD
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
=======
        
>>>>>>> daa46c8 (Revert "psql add 3")
    }
}




