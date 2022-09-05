from django.urls import path
from .views import ProductListView

app_name = 'product'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product'),

]
