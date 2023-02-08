from django.shortcuts import render

def listagem_de_produtos(request):
    contex = {
        'produtos':[
        {'nome': 'uva','preco':1}, 
        {'nome': 'melancia','preco':2},
        {'nome': 'banana','preco': 5}

        ]
    }
    return render(request, 'templates/listagem_de_produtos.html.', contex)

# Create your views here.
