from django.urls import path
from client_side.views import product_list_view, product_detail_view, comment_create_view

urlpatterns = [
    path('', product_list_view, name='product_list'),

    path('product/<slug:product_slug>/',
         product_detail_view, name='product_detail'),

    path('product/<slug:product_slug>/comment_create/',
         comment_create_view, name='comment_create')
]





