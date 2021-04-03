from django import forms
from django.core.validators import RegexValidator

from categoria.models import Categoria
from produto.models import Produto
from projeto import settings


class PesquisaProdutoForm(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False)

    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'qtd_estoque', 'imagem', 'disponivel')
        localized_fields = ('preco',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['descricao'].error_messages={'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['categoria'].error_messages={'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset=Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label='--- Selecione uma categoria ---'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['data_cadastro'].error_messages={'required': 'Campo obrigatório',
                                                     'invalid': 'Data inválida'}
        self.fields['data_cadastro'].input_formats=settings.DATE_INPUT_FORMATS
        self.fields['data_cadastro'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['preco'].min_value=0
        self.fields['preco'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['qtd_estoque'].min_value=0
        self.fields['qtd_estoque'].error_messages={
            'required': 'Campo obrigatório',
            'min_value': 'A quantidade deve ser maior ou igual a zero.'
        }
        self.fields['qtd_estoque'].widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        # self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        # self.fields['imagem'].validators=[
        #     RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        # self.fields['imagem'].widget.attrs.update({'class': 'form-control form-control-sm'})
        # self.fields['imagem'].required = True
        self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        self.fields['imagem'].widget.attrs.update({'class': 'btn btn-outline-secondary btn-sm'})
        self.fields['imagem'].required = True

    def clean_qtd_estoque(self):
        qtd = self.cleaned_data['qtd_estoque']
        if qtd < 100:
            raise ValidationError("Quantidade menor do que 100.")
        return qtd