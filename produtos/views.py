from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from produtos.forms import ProdutoModelForm
from produtos.forms import HttpResponseRedirect
def listagem_de_produtos(request):
        produto = Produto.objects.all()
        produtos_dos_vendedores = [{
                'vendedor': {'nome': 'John Doe'},
                'produtos': produto
        }]       
        context = {'produtos_dos_vendedores': produtos_dos_vendedores}
        return render(request, 'templates/listagem_de_produtos.html.', context)
def detalhamento_produto(request,id):
        produto =get_object_or_404(Produto,pk=id)
        print(produto)
        context = {
                'produto': produto
        }
        return render (request, 'templates/detalhamento_produto.html',context)
def cadastrar_produto(request):
        print(request.POST)
        form = ProdutoModelForm 
        context = {
                'form' : form
        }
        if request.method == 'GET':
                print('É um get')
        if request.method == 'POST':
                form = ProdutoModelForm(request.POST)
                if form.is_valid():
                        form.save()
                        return HttpResponseRedirect('/produtos/')
                
        form = ProdutoModelForm()
        context = {
                'form': form
        }

        return render(request, 'templates/cadastrar_produto.html', context)


# Create your views here.
