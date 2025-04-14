from django.urls import path, include

from . import views

urlpatterns = [
    path("singin/", views.singin, name="singin"),
    path('logout/',views.signout, name="logout"),
    path('home/',views.home, name="home"),
    path('counts/', views.os_servers_counts, name='servers_count')

]