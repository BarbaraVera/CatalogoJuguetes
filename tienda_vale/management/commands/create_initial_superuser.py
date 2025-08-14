# catalogo/management/commands/create_initial_superuser.py

import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe uno.'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            if not username or not email or not password:
                self.stdout.write(self.style.ERROR('Faltan las variables de entorno DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL o DJANGO_SUPERUSER_PASSWORD.'))
                return

            self.stdout.write(self.style.SUCCESS(f'Creando cuenta para {username} ({email})'))
            User.objects.create_superuser(email=email, username=username, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'El usuario "{username}" ya existe.'))