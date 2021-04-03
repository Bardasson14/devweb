from django.contrib import admin
from .models import Fornecedor

class FornecedorAdmin(admin.ModelAdmin):
    fields = ('cnpj', 'nome', 'telefone', 'endereco')
    
    #list_display = ['nome', 'slug', 'categoria', 'imagem', 'qtd_estoque', 'preco', 'disponivel']
    ##search_fields = ['nome', 'imagem']
    #list_filter = ['categoria']
    #list_editable = ['categoria', 'imagem', 'qtd_estoque', 'preco', 'disponivel']
    #prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Fornecedor, FornecedorAdmin)