from django.contrib import admin
from django.urls import path
from .views import listagem_de_produtos, detalhamento_produto, cadastrar_produto

urlpatterns = [
    path('',listagem_de_produtos),
    path('<int:id>', detalhamento_produto),
    path('cadastrar',cadastrar_produto)

]
