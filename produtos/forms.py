from django.forms import ModelForm
from produtos.models import Produto

class ProdutoModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'anunciante', 'imagem']

class ServicoModelForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco', 'anunciante', 'imagem']