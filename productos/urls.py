from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

from productos import views

app_name = 'productos'
urlpatterns = [
    path('', views.home),
    path('lista/', views.lista, name='lista'),
    path('crear/', views.crearProducto, name='crear'),
    path('editar/<int:id_product>', views.crearProducto, name='editar'),
    path('eliminar/<int:id_product>', views.eliminarProducto, name='eliminar')
]
