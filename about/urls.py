from django.urls import path
from .views import Our_services

app_name = 'about'

urlpatterns = [
    path('about', Our_services.as_view(), name='about'),

]
