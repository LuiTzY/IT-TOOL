from django.urls import path

from src.servers.views.servers import *
from src.servers.views.os import *
from .views import *



SERVERS_PATHS = [
    path('servidores/', ServerListView.as_view(), name='server_list'),
    path('servidores/nuevo/', ServerCreateView.as_view(), name='server_create'),
    path('servidores/<int:pk>/editar/', ServerUpdateView.as_view(), name='server_update'),
    path('servidores/<int:pk>/eliminar/', ServerDeleteView.as_view(), name='server_delete'),
    path('servidores/<int:pk>/', ServerDetailView.as_view(), name='server_detail'),
]

OS_PATHS = [   
    path('os/', OSListView.as_view(), name='os_list'),
    path('os/nuevo/', OSCreateView.as_view(), name='os_create'),
    path('os/<int:pk>/editar/', OSUpdateView.as_view(), name='os_update'),
    path('os/<int:pk>/eliminar/', OSDeleteView.as_view(), name='os_delete'),
]

urlpatterns  =  SERVERS_PATHS + OS_PATHS