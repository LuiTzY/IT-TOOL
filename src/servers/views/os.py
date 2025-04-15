from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from ..models import Server, OS
from ..forms import ServerForm,OSForm
 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class OSListView(LoginRequiredMixin,ListView):
    model = OS
    template_name = 'servers/os/os_list.html'
    #variable disponible al renderizar la vista(como si fuera un context)
    context_object_name = 'sistemas'

class OSCreateView(LoginRequiredMixin,CreateView):
    model = OS
    form_class = OSForm
    template_name = 'servers/os/os_form.html'
    success_url = reverse_lazy('os_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Se registro el servidr correctamente")
        messages.success(self.request, f" Sistema '{self.object.server_name}' creado exitosamente.")
        return response

class OSUpdateView(LoginRequiredMixin,UpdateView):
    model = OS
    form_class = OSForm
    template_name = 'servers/os/os_form.html'
    success_url = reverse_lazy('os_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Se registro el servidr correctamente")
        messages.success(self.request, f" Sistema '{self.object.server_name}' actualizado exitosamente.")
        return response


class OSDeleteView(LoginRequiredMixin,DeleteView):
    model = OS
    template_name = 'servers/os/os_confirm_delete.html'
    success_url = reverse_lazy('os_list')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        server_name = self.object.server_name  # Guardamos el nombre antes de borrar
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f"Sistema '{server_name}' eliminado exitosamente.")
        return response