from django.db import models
# Create your models here.
TIPO_PRODUTO ='P'
TIPO_SERVICO = 'S'

class Anunciante (models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    excluido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    TIPOS_CHOICE = [
        (TIPO_PRODUTO, 'Produto'),
        (TIPO_SERVICO, 'servicos')
    ]
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    estoque = models.IntegerField(default=0)
    tipo =models.CharField(max_length=2, choices = TIPOS_CHOICE, default = TIPO_PRODUTO)
    excluido = models.BooleanField(default=False)

    anunciante = models.ForeignKey(Anunciante, on_delete=models.CASCADE)

    imagem = models.ImageField()

    def __str__(self):
        return f' {self.get_tipo_display()}:  {self.nome}'
