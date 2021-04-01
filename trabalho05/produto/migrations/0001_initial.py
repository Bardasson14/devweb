# Generated by Django 3.0.2 on 2020-02-15 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('imagem', models.CharField(blank=True, max_length=50)),
                ('qtd_estoque', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('disponivel', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categoria.Categoria')),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
