from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from fornecedor.forms import PesquisaFornecedorForm, FornecedorForm
from fornecedor.models import Fornecedor

# @login_required(login_url='/autenticacao/login')
# @staff_member_required(login_url='/autenticacao/login')
# @user_passes_test(lambda u: u.is_superuser)
# @user_passes_test(lambda u: u.is_staff)

def lista_fornecedor(request):
    form = PesquisaFornecedorForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_fornecedors = Fornecedor.objects\
                                   .filter(nome__icontains=nome)\
                                   .order_by('nome')
        paginator = Paginator(lista_de_fornecedors, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print("list: ", lista_de_fornecedors)
        print("page_obj: ", page_obj)

        return render(request, 'fornecedor/pesquisa_fornecedor.html', { 'fornecedores': page_obj,
                                                                  'form': form,
                                                                  'nome': nome })
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar recuperar um fornecedor.')


# @user_passes_test(lambda u: u.is_staff)
def cadastra_fornecedor(request):
    print(request)
    if request.POST:
        fornecedor_id = request.session.get('fornecedor_id')
        
        if fornecedor_id:
            fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
            fornecedor_form = FornecedorForm(request.POST, request.FILES, instance=fornecedor)
        else:
            fornecedor_form = FornecedorForm(request.POST, request.FILES)

        if fornecedor_form.is_valid():
            fornecedor = fornecedor_form.save(commit=False)
            fornecedor.save()
            if fornecedor_id:
                messages.add_message(request, messages.INFO, 'Fornecedor alterado com sucesso!')
                del request.session['fornecedor_id']
            else:
                messages.add_message(request, messages.INFO, 'Fornecedor cadastrado com sucesso!')

            return redirect('fornecedor:exibe_fornecedor', id=fornecedor.id)
    else:
        
        try:
            del request.session['fornecedor_id']
        except KeyError:
            pass
        fornecedor_form = FornecedorForm()

    return render(request, 'fornecedor/cadastra_fornecedor.html', {'form': fornecedor_form})


# @user_passes_test(lambda u: u.is_staff)
def exibe_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    request.session['fornecedor_id_del'] = id
    return render(request, 'fornecedor/exibe_fornecedor.html', {'fornecedor': fornecedor})


# @user_passes_test(lambda u: u.is_staff)
def edita_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    fornecedor_form = FornecedorForm(instance=fornecedor)
    request.session['fornecedor_id'] = id
    return render(request, 'fornecedor/cadastra_fornecedor.html', {'form': fornecedor_form})


# @user_passes_test(lambda u: u.is_staff)
def remove_fornecedor(request):
    fornecedor_id = request.session.get('fornecedor_id_del')
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    fornecedor.delete()
    del request.session['fornecedor_id_del']
    messages.add_message(request, messages.INFO, 'Fornecedor removido com sucesso.')
    return lista_fornecedor(request)



