from django.shortcuts import render

def listagem_de_produtos(request):

    
        produtos_de_vendedores = [{
            'vendedor': {'nome': 'john Doe'},
            'produtos':[
                {'nome': 'uva','preco':1}, 
                {'nome': 'melancia','preco':2},
                {'nome': 'banana','preco': 5}
        ]
        }]
        context = {'produtos_de_vendedores': produtos_de_vendedores}
    
        return render(request, 'templates/listagem_de_produtos.html.', context)

# Create your views here.
