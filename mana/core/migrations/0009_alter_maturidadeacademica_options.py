# Generated by Django 3.2.5 on 2021-11-04 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211102_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maturidadeacademica',
            options={'ordering': ['id'], 'verbose_name': 'Maturidade acadêmica', 'verbose_name_plural': 'Maturidades acadêmica'},
        ),
    ]