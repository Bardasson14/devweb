from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('categoria', 'nome', 'qtd', 'preco')

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(self, *args, **kwargs)
        for key in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })