from django.contrib import admin
from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static

#esto permite identificar a todo el conjunto de urls
app_name='persona_app'

urlpatterns = [

    path('', InicioView.as_view(), name = 'inicio_empleado'),
    path('listar-empleados/', ListAllEmpleado.as_view(), name = 'empleados_all'),
    path('listar-by-area/<shorname>', ListByArea.as_view(), name='empleado_area'),
    path('buscar-empleado/', ListEmpleadoByKword.as_view()),
    path('listar-habilidades/', ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', EmpleadoCreateView.as_view(), name='nuevo_empleado'),
    path('success/', SuccessView.as_view(), name = 'correcto'), # name permite identificar a esa url en especifico
    path('update-empleado/<pk>/', EmpleadoUpdateView.as_view(), name = 'modificar_empleado'),
    path('delete-empleado/<pk>/', EmpleadoDeleteView.as_view(), name = 'eliminar_empleado'),
    path('listar-empleados-admin/', ListEmpleadoAdmin.as_view(), name = 'empleados_admin'),
] 