# Generated by Django 3.1.7 on 2021-03-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmreview', '0007_auto_20210326_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avaliation',
            field=models.FloatField(null=True),
        ),
    ]
