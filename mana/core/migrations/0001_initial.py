# Generated by Django 3.2.5 on 2021-12-15 23:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaAtuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Área de atuação',
                'verbose_name_plural': 'Áreas de atuação',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cultura',
                'verbose_name_plural': 'Culturas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendaria', models.BooleanField(default=True, null=True)),
                ('sugestao', models.TextField(default='', null=True)),
                ('recrutador', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='MaturidadeAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Maturidade acadêmica',
                'verbose_name_plural': 'Maturidades acadêmica',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MaturidadeProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Maturidade profissional',
                'verbose_name_plural': 'Maturidades profissionais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Prêmio',
                'verbose_name_plural': 'Prêmios',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Startup',
                'verbose_name_plural': 'Startups',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('areas_atuacao', models.ManyToManyField(to='core.AreaAtuacao')),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cultura')),
                ('habilidades', models.ManyToManyField(to='core.Habilidade')),
                ('maturidade_academica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.maturidadeacademica')),
                ('maturidade_profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.maturidadeprofissional')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.startup')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.startup')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('linkedin_url', models.CharField(max_length=255)),
                ('areas_atuacao', models.ManyToManyField(to='core.AreaAtuacao')),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='culturas', to='core.cultura')),
                ('habilidades', models.ManyToManyField(blank=True, to='core.Habilidade')),
                ('maturidade_academica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.maturidadeacademica')),
                ('maturidade_profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maturidades_profissionais', to='core.maturidadeprofissional')),
                ('premios', models.ManyToManyField(blank=True, to='core.Premio')),
                ('projetos', models.ManyToManyField(blank=True, to='core.Projeto')),
                ('startups', models.ManyToManyField(blank=True, to='core.Startup')),
            ],
            options={
                'verbose_name': 'Profissional',
                'verbose_name_plural': 'Profissionais',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='NPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('sugestao', models.CharField(default='', max_length=500)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.vaga')),
            ],
            options={
                'verbose_name': 'Nota',
                'verbose_name_plural': 'Nota',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(default=0, null=True)),
                ('contrataria', models.BooleanField(default=True, null=True)),
                ('posicao_lista', models.IntegerField(default=0, null=True)),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.experimento')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.profissional')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.vaga')),
            ],
        ),
        migrations.CreateModel(
            name='Endocos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacoes', models.IntegerField(default=0)),
                ('recomendado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profissional')),
            ],
            options={
                'verbose_name': 'Recomendação de habilidade',
                'verbose_name_plural': 'Recomendações de habilidades',
            },
        ),
    ]
