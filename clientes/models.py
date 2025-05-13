from django.db import models
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    veiculo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nome} - {self.placa}"

