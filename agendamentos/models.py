# agendamentos/models.py

from django.db import models
from clientes.models import Cliente
from servicos.models import Servico

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('Aguardando', 'Aguardando'),
        ('Em Lavagem', 'Em Lavagem'),
        ('Finalizado', 'Finalizado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos_cliente')  # Adicionado related_name
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='agendamentos_servico')  # Adicionado related_name
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando')  # Adicionando o campo status
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} em {self.data} às {self.hora}"
