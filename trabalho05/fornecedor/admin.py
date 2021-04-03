from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    fields = ('cnpj', 'nome', 'telefone', 'endereco')

admin.site.register(Fornecedor, FornecedorAdmin)