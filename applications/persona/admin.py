from django.contrib import admin

from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    #coloca las columnas deseas en el admin site
    list_display=('first_name', 'last_name', 'departamento', 'job','full_name')
    
    #obj significa el contexto de los valores  que esta iterando 
    '''def full_name(self, obj):
        return obj.first_name +  ' ' + obj.last_name'''



    #coloca una caja de busqueda
    search_fields= ('first_name',)
    #coloca un apartado de filtrado
    list_filter =('job', 'habilidad')

    #esto cambia la interfaz de la relacion muchos a muchos
    filter_horizontal=('habilidad',)



admin.site.register(Empleado, EmpleadoAdmin)