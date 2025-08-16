#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
# 2. Instalar las dependencias de Node.js (incluyendo Tailwind)
npm install

# 3. Compilar el CSS de Tailwind para producción
npm run build

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_initial_superuser