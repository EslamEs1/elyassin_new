from django.urls import path
from .views import main,contact

app_name = 'home'

urlpatterns = [
    path('', main, name='main'),
    path('contact/', contact, name='contact')


]
