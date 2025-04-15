from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

#Vistas 
class DNSListView(LoginRequiredMixin,ListView):
    model = DNS
    template_name = 'dns/dns_list.html'
    context_object_name = 'dns'

class DNSCreateView(LoginRequiredMixin,CreateView):
    model = DNS
    form_class = DNSForm
    template_name = 'dns/dns_form.html'
    success_url = reverse_lazy('dns-list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"DNS '{self.object.server_name}' creado exitosamente.")
        return response

class DNSUpdateView(LoginRequiredMixin,UpdateView):
    model = DNS
    form_class = DNSForm
    template_name = 'dns/dns_form.html'
    success_url = reverse_lazy('dns-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"DNS '{self.object.server_name}' actualizado exitosamente.")
        return response
    
class DNSDeleteView(LoginRequiredMixin,DeleteView):
    model = DNS
    template_name = 'dns/dns_confirm_delete.html'
    success_url = reverse_lazy('dns-list')
    
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        server_name = self.object.server_name  # Guardamos el nombre antes de borrar
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f"DNS '{server_name}' eliminado exitosamente.")
        return response

class DNSDetailView(LoginRequiredMixin,DetailView):
    model = DNS
    template_name = 'dns/dns_detail.html'
    context_object_name = 'dns'





#Vistas para las entradas dns

class DNSEntryListView(LoginRequiredMixin,ListView):
    model = DNSEntry
    template_name = 'dns/entry/dns_entry_list.html'
    context_object_name = 'entry'

class DNSEntryCreateView(LoginRequiredMixin,CreateView):
    model = DNSEntry
    form_class = DNSEntryForm
    template_name = 'dns/entry/dns-entry_form.html'
    success_url = reverse_lazy('dns_entry_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f" Entrada DNS '{self.object.entry_name}' creado exitosamente.")
        return response


class DNSEntryUpdateView(LoginRequiredMixin,UpdateView):
    model = DNSEntry
    form_class = DNSEntryForm
    template_name = 'dns/entry/dns-entry_form.html'
    success_url = reverse_lazy('dns_entry_list')
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f" Entrada DNS '{self.object.entry_name}' actualizado exitosamente.")
        return response

class DNSEntryDeleteView(LoginRequiredMixin,DeleteView):
    model = DNSEntry
    template_name = 'dns/entry/dns-entry_confirm_delete.html'
    success_url = reverse_lazy('dns_entry_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        server_name = self.object.entry_name  # Guardamos el nombre antes de borrar
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f"Entrada DNS '{server_name}' eliminado exitosamente.")
        return response

class DNSEntryDetailView(LoginRequiredMixin,DetailView):
    model = DNSEntry
    template_name = 'dns/entry/dns-entry_detail.html'
    context_object_name = 'entry'
