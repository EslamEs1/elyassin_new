from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    summernote_fields = '__all__'

