from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table='categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    # def get_absolute_url(self):
    #    return reverse('carrinho:lista_produtos_por_categoria', args=[self.slug])

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    qtd = models.IntegerField()
    preco = models.FloatField()

    class Meta:
        db_table = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.nome
 