# Generated by Django 3.1.7 on 2021-03-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmreview', '0012_auto_20210327_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_dir',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
