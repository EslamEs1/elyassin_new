from django.contrib import admin
from .models import Settings, Message
# Register your models here.


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if Settings.objects.count() >= 1 else True




@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['name', 'email', 'subject', 'created']
    list_filter = ['name',  'created']