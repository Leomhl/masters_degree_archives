# Generated by Django 3.2.5 on 2021-11-02 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211102_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recomendacaoprofissional',
            old_name='premios',
            new_name='habilidades',
        ),
    ]
