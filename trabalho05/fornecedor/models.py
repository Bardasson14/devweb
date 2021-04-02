from django.db import models
from django.urls import reverse
#from categoria.models import Categoria

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, db_index=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13, unique=True)
    endereco = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table='fornecedor'

    def __str__(self):
        return self.nome





