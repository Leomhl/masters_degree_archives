# Generated by Django 3.2.5 on 2021-11-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_startup_cultura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomendacaoprofissional',
            name='descricao',
        ),
        migrations.AddField(
            model_name='recomendacaoprofissional',
            name='premios',
            field=models.ManyToManyField(blank=True, to='core.Habilidade'),
        ),
    ]
