from django.urls import reverse
from django.db import models
from django.utils.text import slugify  


class Post (models.Model):
    image = models.ImageField(upload_to = 'post', verbose_name='image')
    title = models.CharField(max_length=100, verbose_name='title')
    text = models.TextField(max_length=15000, verbose_name='text')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    slug = models.SlugField(max_length=100, verbose_name='Dont Touch This')

    #Metadata
    class Meta :
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('blog:post_detail', args={self.slug})

    def __str__(self):
        return self.title