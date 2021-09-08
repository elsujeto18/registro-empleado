from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView,CreateView,TemplateView, UpdateView, DeleteView


from .models import Empleado
from .forms  import EmpleadoForm

from django.urls import reverse_lazy


class InicioView(TemplateView):
    template_name ='inicio.html'


class ListAllEmpleado(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4
    #cuando le colocas el queryset no necesitas especificar un model
    #model = Empleado
    context_object_name = 'lista'

    def get_queryset(self):
        
        palabra_clave=self.request.GET.get("kword", '')
        
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
         )
        return lista


# para el boton administrar
class ListEmpleadoAdmin(ListView):
    template_name = 'empleado/list_empleados.html'
    paginate_by = 10
    model = Empleado
    context_object_name = 'lista'

    


#no es la mejor forma de hacer filtro en los listviews   
'''class ListByArea(ListView):
    template_name = 'empleado/list_by_area.html'
    queryset = Empleado.objects.filter(departamento__shor_name = 'Comerciales' )'''


class ListByArea(ListView):
    template_name = 'empleado/list_by_area.html'

    def get_queryset(self):
        #kwargs me permite acceder a ese parametro de los urls
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(departamento__shor_name = area )
        
        return lista


class ListEmpleadoByKword(ListView):
    template_name='empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        
        palabra_clave=self.request.GET.get("kword", '')
       
        lista = Empleado.objects.filter(first_name = palabra_clave )
        return lista

#cuando existe una relacion de muchos a muchos
class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/list_habilidad.html'
    context_object_name ='habilidad'

    def get_queryset(self):
        nombre=self.request.GET.get("name",)
        
        empleado = Empleado.objects.get(first_name=nombre)
        
        return empleado.habilidad.all()



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']= 'Empleado del mes'
        return context



class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    form_class = EmpleadoForm
    #fields = ['first_name','last_name','job','departamento','habilidad'] #cuando trabajamos con forms personalizados se utiliza el form_class
    #fields = ('__all__') #para traer todos los campos del modelo empleado

    #success_url = '.' para que se recargue la misma pagina

    #debe estar todo pegado, ya que puede dar error por reconocer el espacio como string
    success_url = reverse_lazy('persona_app:empleados_admin') 

    def form_valid(self, form):
        empleado = form.save(commit=False) # para no tener que guardar, si no solo almacenar los datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = ['first_name','last_name','job','departamento','habilidad']
    success_url = reverse_lazy('persona_app:empleados_admin') 

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin') 


    