from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import AunthenticaUser, UserForm

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


from src.dns.models import * 
from src.servers.models import *
from django.http import JsonResponse


def os_servers_counts(request):
    context = {}
    servers = Server.objects.all()
    servers_types = { 
        
        "Linux":servers.filter(server_os__os_type='Linux').count(),
        "Windows":servers.filter(server_os__os_type='Windows').count()
    }
    context['servers_type'] = servers_types

    return JsonResponse (context)

#vista principal de la app

def home(request):
    context = {}
    
    servers = Server.objects.all()
    servers_count = servers.count()
    
    os =  OS.objects.all().count()
    dns_servers =  DNS.objects.all().count()
    dns_entrys =  DNSEntry.objects.all().count()
    
    servers_types = { 
        
        "Linux":servers.filter(server_os__os_type='Linux').count(),
        "Windows":servers.filter(server_os__os_type='Windows').count()
    }
    
    context['servers_type'] = servers_types
    context['servers'] = servers_count
    context['os'] = os
    context['dns'] = dns_servers
    context['dns_entrys'] =  dns_entrys
    context['last_added_servers'] = servers.order_by("-created_at")
    return render(request,'layout/dashboard.html', context)


#View para iniciar sesion del usuario
def singin(request):
    if request.method == "GET":
        return render(request, "authentication/singin.html",{"form":AunthenticaUser()}) 
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)   
        
        if user is None:
            messages.error(request,"El correo electronico o contraseña nos son validos")
            return render(request, "authentication/singin.html",{"form":AunthenticaUser(),"welcome":True})
        
        login(request,user)
        
        messages.success(request, '¡Has iniciado sesion correctamente!')
        return redirect("home")
        
#View para cerrar sesion del usuario
@login_required
def signout(request):
    try:
        logout(request)
    except Exception as e:
        messages.error(request,"No se ha podido cerrar sesion correctamente.")
    else:
        messages.success(request,"¡¡ Has cerrado sesion correctamente !!")
    return redirect('singin')

#View para cargar perfil del usuario