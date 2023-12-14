#!/bin/bash

# Move to app directory
cd raptorWebApp

# Migrate database
conda run -n djangoWork python manage.py migrate

# Collect static files for serving
conda run -n djangoWork python manage.py collectstatic --noinput

# Create superuser if no users exist
conda run -n djangoWork python manage.py createSuper

# Run Django development server, NOT suitable for production!
conda run -n djangoWork python manage.py runserver 0.0.0.0:80