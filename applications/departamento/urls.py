from django.contrib import admin
from django.urls import path
from . import views

app_name='departamento_app'

urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='new_departamento'),
    path('lista_departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    
]