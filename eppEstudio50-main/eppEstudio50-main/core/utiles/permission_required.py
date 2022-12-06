# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse


class PermissionRequiredMixin(AccessMixin):
    """
    CBV Mixin: Verifica que el usuario actual posea los permisos especificados.
    """
    permission = None

    def get_permission(self):
        if self.permission is None:
            raise ImproperlyConfigured(
                '{0} is missing the permission_required attribute. Define {0}.permission_required, or override '
                '{0}.get_permission_required().'.format(self.__class__.__name__)
            )
        return self.permission

    def dispatch(self, request, *args, **kwargs):
        # Verifica primero que el usuario actual se encuentre autenticado.
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not request.user.has_perm(self.get_permission()):
            if settings.DEBUG:
                return HttpResponseRedirect(reverse('inicio'))
            else:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)