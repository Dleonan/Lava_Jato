from django.db import models
from clientes.models import Cliente
from servicos.models import Servico

class Caixa(models.Model):
    aberto_em = models.DateTimeField(auto_now_add=True)
    fechado_em = models.DateTimeField(null=True, blank=True)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    aberto = models.BooleanField(default=True)

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    caixa = models.ForeignKey(Caixa, on_delete=models.PROTECT)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    valor = models.DecimalField(max_digits=10, decimal_places=2)