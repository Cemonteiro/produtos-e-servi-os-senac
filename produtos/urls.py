from django.contrib import admin
from django.urls import path
from .views import listagem_de_produtos,listagem_de_servicos, detalhamento_produto, cadastrar_produto, excluir, alterar

urlpatterns = [
    path('',listagem_de_produtos),
    path('',listagem_de_servicos),
    path('<int:id>', detalhamento_produto),
    path('cadastrar',cadastrar_produto),
    path('<int:id>/excluir', excluir),
    path('<int:id>/alterar', alterar)

]
