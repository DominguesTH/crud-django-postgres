# Generated by Django 4.1.5 on 2023-01-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='descricao',
            field=models.CharField(max_length=220),
        ),
    ]