"""produto_e_serviços URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from produtos.views import listagem_de_servicos, cadastrar_servico

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('produtos/', include('produtos.urls')),
    path('servicos/',listagem_de_servicos),
    path('servicos/cadastrar/', cadastrar_servico, name='cadastro_servico')
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
