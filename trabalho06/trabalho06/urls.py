from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cadastra_produto/', views.cadastra_produto, name='cadastra_produto'),
    path('lista_produtos/', views.lista_produtos, name='lista_produtos'),
    path('registra_produto/', views.registra_produto, name='registra_produto'),
    path('remove_produto/<int:id>', views.remove_produto)
]