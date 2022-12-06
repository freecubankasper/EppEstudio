"""scp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from core.utiles import ajax as ajax_views

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, logout_then_login
from django.urls import path, include

from core.views.especialidades import EspecialidadesView
from core.views.gestionlista import Adicionarmilista
from core.views.inicia import IniciaView
from core.views.inicio import InicioView
from core.views.about import AboutView
from core.views.catalog import CatalogView
from core.views.misproyectos import MisProyectosView
from core.views.talent import TalentView
from core.views.partners import PartnersView
from core.views.equipment import EquipmentView
from evento.views.evento_proyecto import RegistrarEventoProyectoCalendarioView
from core.views.calendario import CalendarioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciar-sesion/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
         name='iniciar_sesion'),
    path('iniciar-sesion-cliente/', LoginView.as_view(template_name='home-13.html',redirect_authenticated_user=True),
         name='iniciar_sesion_cliente'),
    path('', IniciaView.as_view(),
         name='inicio'),
    path('about/', AboutView.as_view(),
         name='about'),
    path('talent/', TalentView.as_view(),
         name='talent'),
    path('proyects/', MisProyectosView.as_view(),
         name='proyects'),
    path('equipment/', EquipmentView.as_view(),
         name='equipment'),
    path('especialidades/', EspecialidadesView.as_view(),
         name='especialidades'),
    path('partners/', PartnersView.as_view(),
         name='partners'),
    # path('calendario/', CalendarioView.as_view(),
    #      name='calendario'),
    path('calendario/<int:proyecto_id>/eventos/', CalendarioView.as_view(),
         name='calendario'),
    path('adicionarmilista/<int:producto_id>/<int:subcategoria>/<str:nombre>/<int:cantidad>', Adicionarmilista.as_view(),
         name='adicionar_milista'),


    # path('talentdetail/<integer:inc_number>/', TalentdetailView.as_view() name='talentdetail'),
    # path('iniciar-sesion/', MyLoginView.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', logout_then_login, name='cerrar_sesion'),
    path('inicio-admin', InicioView.as_view(), name='inicio_admin'),

    # Includes
    path('', include('usuario.urls')),
    path('', include('proyecto.urls')),
    path('', include('nomencladores.urls')),
    path('', include('actor.urls')),
    path('', include('evento.urls')),
    path('', include('equipo_proteccion_personal.urls')),
    path('', include('reporte_nominal.urls')),
    path('', include('equipamiento.urls')),
    path('', include('locacion.urls')),
    path('', include('llamado.urls')),
    path('', include('transporte.urls')),
    path('', include('abastecimiento.urls')),
    path('', include('especialista.urls')),
    path('crear_modal__detalles_equipamiento/', ajax_views.DetallesEquipamientoAjaxView.as_view()),
    path('crear_modal_detalles_talento/', ajax_views.DetallesTalentoAjaxView.as_view()),
    path('adicionarequipamiento/<int:proyecto_id>/<int:llamado_id>', ajax_views.DetallesEquipamientoAjaxView.as_view()),

    # path('', include('core.urls')),

]


    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
