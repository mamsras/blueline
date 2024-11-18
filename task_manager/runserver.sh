#!/bin/bash

# Définir DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE="task_manager.settings"

# Activer l'environnement virtuel
source /home/mamisoa/my_code/blueline/.venv/bin/activate

# Lancer Daphne sur le port 8001
daphne -p 8001 task_manager.routing:application &

# Lancer le serveur de développement Django sur un autre port (par exemple 8000)
python manage.py runserver

# Arrêter Daphne lorsque le script se termine
trap "pkill -P $$" EXIT
