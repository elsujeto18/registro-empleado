from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
from django.views.generic import ListView

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'


    def form_valid(self, form):
        print('estamos en el form valid')

        #si hacemos de esta manera es importante poner despues el .save()
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        # ya que estamos especificando el .create() no necesitamos colocarle el .save()
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/list_departamentos.html"
    context_object_name = 'departamentos'

