from django.urls import path
from app_tienda import views

# app_name = 'app_tienda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('clientes/<str:pk_test>/', views.clientes, name='clientes'),
]
