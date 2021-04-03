from django import forms
from django.core.validators import RegexValidator, ValidationError

from categoria.models import Categoria
from fornecedor.models import Fornecedor
from projeto import settings

from localflavor.br.forms import BRCNPJValidator


class PesquisaFornecedorForm(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False)

    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('cnpj', 'nome', 'telefone', 'endereco')
        # localized_fields = ('preco',) -> telefone e CNPJ

    def __init__(self, *args, **kwargs):
        # adicionar validacao de CNPJ
        super().__init__(*args, **kwargs)

        self.fields['cnpj'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'CNPJ duplicado.'}
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['cnpj'].validators=[RegexValidator(regex=r'([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})', message='CNPJ Inválido'), self.cnpj_validator]

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['telefone'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Telefone duplicado.'}
        self.fields['telefone'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['endereco'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Endereço duplicado.'}
        self.fields['endereco'].widget.attrs.update({'class': 'form-control form-control-sm'})

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        for char in ['.', '-', '/']:
            cnpj = cnpj.replace(char, '')
        return cnpj

    def cnpj_validator(self, value):
        if (value.isdecimal() and len(value)>14):
            raise ValidationError('CNPJ contém mais do que 14 dígitos numéricos')
        return value