from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from ..models import Server, OS
from ..forms import ServerForm,OSForm
from django.contrib import messages


class ServerListView(ListView):
    model = Server
    template_name = 'servers/server_list.html'
    context_object_name = 'servers'

class ServerCreateView(CreateView):
    model = Server
    form_class = ServerForm
    template_name = 'servers/server_form.html'
    success_url = reverse_lazy('server_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Se registro el servidr correctamente")
        messages.success(self.request, f" Servidor '{self.object.server_name}' creado exitosamente.")
        return response

class ServerUpdateView(UpdateView):
    model = Server
    form_class = ServerForm
    template_name = 'servers/server_form.html'
    success_url = reverse_lazy('server_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Se registro el servidr correctamente")
        messages.success(self.request, f" Servidor '{self.object.server_name}' actualizado exitosamente.")
        return response
    
    
class ServerDeleteView(DeleteView):
    model = Server
    template_name = 'servers/server_confirm_delete.html'
    success_url = reverse_lazy('server_list')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        server_name = self.object.server_name  # Guardamos el nombre antes de borrar
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f"Servidor '{server_name}' eliminado exitosamente.")
        return response
    
class ServerDetailView(DetailView):
    model = Server
    template_name = 'servers/server_detail.html'
    context_object_name = 'server'
