# Generated by Django 3.1.7 on 2021-03-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmreview', '0006_auto_20210326_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='sinopsis',
            field=models.TextField(blank=True, null=True),
        ),
    ]