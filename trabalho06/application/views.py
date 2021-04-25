from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from application.models import *
from .forms import ProdutoForm

def index(request):
    return render(request, 'index.html')

def cadastra_produto(request):
    return render(request, 'cadastra_produto.html', {'categorias': Categoria.objects.all()})

@csrf_exempt
def registra_produto(request):
    print(request.body)
    if request.is_ajax and request.POST:
        form = ProdutoForm(request.POST)
        form.save()
        return HttpResponse(200)
    else:
        return HttpResponse(400)

def lista_produtos(request):
    return render(request, 'lista_produtos.html', { 'produtos': Produto.objects.all()})