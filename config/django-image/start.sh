#!/bin/bash

cd /usr/src/app

echo "Iniciando contenedor Django"

if [ ! -f manage.py ]; then

    echo "Proyecto Django inexistente. Creando..."
    django-admin startproject proyecto .

fi

echo "Generando Migraciones"

python manage.py makemigrations

echo "Aplicando Migraciones"

python manage.py migrate

echo "Verificando superusuario"

python manage.py shell << EOF

from django.contrib.auth import get_user_model 

User = get_user_model()

if not User.objects.filter(
    username="${DJANGO_SUPERUSER_USERNAME}"
).exists():

    User.objects.create_superuser(
        "${DJANGO_SUPERUSER_USERNAME}",
        "${DJANGO_SUPERUSER_EMAIL}",
        "${DJANGO_SUPERUSER_PASSWORD}"
    )
EOF

echo "Iniciando servidor Django"

python manage.py runserver 0.0.0.0:8000
