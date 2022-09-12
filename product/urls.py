from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'product'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),
    path('product/detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

]
