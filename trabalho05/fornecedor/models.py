from django.db import models
from django.urls import reverse

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13, unique=True)
    endereco = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table='fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('fornecedor:exibe_fornecedor', args=[self.id])

