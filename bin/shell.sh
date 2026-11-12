#!/bin/bash

echo "Abriendo Django Shell"

docker compose exec django python manage.py shell