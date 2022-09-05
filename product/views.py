from unicodedata import category
from urllib import request
from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView
from django.db.models import  Q


class ProductListView(ListView):
    model =  Product
    template_name = 'product_list.html'

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        if search_query:
            return Product.objects.filter(category__title=search_query)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

            

