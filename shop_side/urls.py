from django.urls import path
from .views import product_create_view, product_delete_view, product_update_view

urlpatterns = [
    path('product-create/', product_create_view,
         name='product_create'),
    path('product-delete/<slug:product_slug>/',
         product_delete_view, name='product_delete'),
    path('product-update/<slug:product_slug>/',
         product_update_view, name='product_update')
]


