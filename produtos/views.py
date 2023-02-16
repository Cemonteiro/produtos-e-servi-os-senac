from django.shortcuts import render, get_object_or_404
from produtos.models import Produto,TIPO_PRODUTO,TIPO_SERVICO
from produtos.forms import ProdutoModelForm
from django.http import HttpResponseRedirect

def listagem_de_produtos(request):
        produto = Produto.objects.filter(tipo=TIPO_PRODUTO, excluido=False)
        produtos_dos_vendedores = [{
                'vendedor': {'nome': 'John Doe'},
                'produtos': produto
        }]       
        context = {'produtos_dos_vendedores': produtos_dos_vendedores}
        return render(request, 'templates/listagem_de_produtos.html', context)


def listagem_de_servicos(request):   
        servicos  = Produto.objects.filter(tipo=TIPO_SERVICO, excluido=False) 
        context = {}
        return render(request, 'templates/listagem_de_servicos.html', context)

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
def excluir (request, id):
        produto =get_object_or_404(Produto,pk=id)
        if request.method == 'POST':
                produto.excluido = True
                produto.save()
                return HttpResponseRedirect('/produtos/')        
        print(produto)
        context = {
                'produto': produto
        }
        return render(request, 'templates/excluir.html', context)
def alterar (request, id):
        produto =get_object_or_404(Produto, pk=id)
        if request.method == 'POST':
                form = ProdutoModelForm(request.POST)
                if form.is_valid():
                        print(form.cleaned_data)
                        produto.nome = form.cleaned_data['nome']
                        produto.estoque = form.cleaned_data['estoque']
                        produto.preco = form.cleaned_data['preco']
                        produto.save()
                        return HttpResponseRedirect(f'/produtos/{produto.id}')
        form = ProdutoModelForm(instance=produto)
        context = {
                'form': form
        }
        return render(request, 'templates/alterar_produto.html', context)
# Create your views here.
