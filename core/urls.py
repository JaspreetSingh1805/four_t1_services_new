from django.urls import path
from .views import HomeView, ServicesView, CalloutMaintenanceView, contact_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('callout-maintenance/', CalloutMaintenanceView.as_view(), name='callout_maintenance'),
    path('contact/', contact_view, name='contact'),
]
