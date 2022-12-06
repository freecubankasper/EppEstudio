# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Group, Permission

from usuario.models import User
from django.core.management.base import BaseCommand
# from nomencladores.models.organismo import Organismo


class Command(BaseCommand):

    args = ''
    help = "Type 'manage.py setup --help' for usage."

    def handle(self, *args, **options):

        try:
            User.objects.get(username='admin')
            print("\nYa se encuentra registrado el usuario 'admin'")
        except:
            print("\nCreando usuario administrador.")

            admin_group, _ = Group.objects.get_or_create(name='Admin')
            all_permissions = Permission.objects.all()
            admin_group.permissions.add(*all_permissions)

            user = User.objects.create_superuser(
                username='admin',
                first_name='System Administrator',
                email='admin@admin.cu',
                password='admin123***',
                is_active=True,
                is_staff=True,
                is_superuser=True,
                # rol=admin_rol,  # administrador
            )
            user.groups.add(admin_group)

            print("\nUsuario 'admin' creado con éxito......\n")

