from django.urls import path
from .views import listagem_de_produtos

urlpatterns = [
    path("",listagem_de_produtos)
]
