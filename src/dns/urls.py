from django.urls import path

from .views import *

DNS_PATHS = [
    path('dns/', DNSListView.as_view(), name='dns-list'),
    path('dns/add/', DNSCreateView.as_view(), name='dns-add'),
    path('dns/<int:pk>/edit/', DNSUpdateView.as_view(), name='dns_update'),
    path('dns/<int:pk>/delete/', DNSDeleteView.as_view(), name='dns_delete'),
]

DNS_ENTRY_PATHS = [
    path('dns-entry/', DNSEntryListView.as_view(), name='dns_entry_list'),
    path('dns-entry/add/', DNSEntryCreateView.as_view(), name='dns_entry_add'),
    path('dns-entry/<int:pk>/edit/', DNSEntryUpdateView.as_view(), name='dns_entry_update'),
    path('dns-entry/<int:pk>/delete/', DNSEntryDeleteView.as_view(), name='dns_entry_delete'),
]

urlpatterns = DNS_PATHS + DNS_ENTRY_PATHS
