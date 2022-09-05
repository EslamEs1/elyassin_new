from django.shortcuts import render
from .models import About, Our_Services, Img_services, Our_Team
from django.views.generic import ListView
# Create your views here.


class Our_services(ListView):
    model = Our_Services
    template_name = 'about.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.last()
        context['our_team'] = Our_Team.objects.all()
        return context