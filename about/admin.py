from django.contrib import admin
from .models import About, Our_Services, Img_services, Our_Team
# Register your models here.



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if About.objects.count() >= 1:
            return False
        else:
            return True



@admin.register(Our_Services)
class Our_ServicesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Our_Services.objects.count() >= 4:
            return False
        else:
            return True



@admin.register(Img_services)
class Img_servicesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if Img_services.objects.count() >= 12 else True


@admin.register(Our_Team)
class Our_TeamAdmin(admin.ModelAdmin):
    pass