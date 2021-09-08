from django.shortcuts import render

#vistas genericas

from django.views.generic import TemplateView,CreateView

from django.urls import reverse_lazy



class PruebaView(TemplateView):
    template_name = 'prueba.html'


class EmpleadoCreateView(CreateView):
    model = ''
    template_name = "empleado/add.html"
    fields = ['first_name','last_name','job','departamento']
    #fields = ('__all__') #para traer todos los campos del modelo empleado

    #success_url = '.' para que se recargue la misma pagina

    #debe estar todo pegado, ya que puede dar error por reconocer el espacio como string
    success_url = reverse_lazy('persona_app:correcto') 

    def form_valid(self, form):
        empleado = form.save(commit=False) # para no tener que guardar, si no solo almacenar los datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)