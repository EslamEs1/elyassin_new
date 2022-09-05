from django.urls import reverse
from django.db import models



class Product(models.Model):
    category = models.ForeignKey('Category', related_name='ProductCategory', on_delete=models.CASCADE)
    available = models.BooleanField(default=True, null=True, verbose_name='available')
    img = models.ImageField(upload_to='Product', verbose_name='Product Img')
    title = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField(max_length=15000, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20, null=True, verbose_name='Color')
    slug = models.SlugField(max_length=100, null=True, verbose_name='Slug')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Updated On')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created At')


    class Meta:
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('product:product_detail', args={self.slug})


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Category')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Category"s'

    def __str__(self):
        return self.title
