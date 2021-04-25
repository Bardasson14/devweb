from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from application.models import *
from .forms import ProdutoForm

def index(request):
    return render(request, 'index.html')

def cadastra_produto(request):
    return render(request, 'cadastra_produto.html', {'categorias': Categoria.objects.all()})

def registra_produto(request):
    data = {}

    if request.POST: 

        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.save()
            data['success'] = "Produto cadastrado com sucesso."
            return JsonResponse(data)

        data['error'] = "Erro ao cadastrar produto."
        return JsonResponse(data)

def remove_produto(request, id):
    if request.POST: 
        produto = get_object_or_404(Produto, pk=id)
        produto.delete()
        data = {}
        data['success'] = "Produto removido com sucesso."
        return JsonResponse(data)
    
def atualiza_produto(request, id):
    if request.POST:
        produto = get_object_or_404(Produto, pk=id)
        produto.qtd = request.POST.get('qtd')
        produto.save()
        return JsonResponse({'success': "Produto atualizado com sucesso"})
    
def lista_produtos(request):
    produtos = Produto.objects.all()
    total = 0
    for produto in produtos:
        total += produto.qtd * produto.preco
    return render(request, 'lista_produtos.html', { 'produtos': Produto.objects.all(), 'total': total})