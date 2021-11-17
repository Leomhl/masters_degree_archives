from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Cultura(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Cultura")
        verbose_name_plural = ("Culturas")

    nome = models.CharField(max_length=255)

class AreaAtuacao(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Área de atuação")
        verbose_name_plural = ("Áreas de atuação")

    nome = models.CharField(max_length=255)


class Startup(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Startup")
        verbose_name_plural = ("Startups")

    nome = models.CharField(max_length=255)
    area = models.ForeignKey(AreaAtuacao, on_delete=models.CASCADE)
    # cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)


class Projeto(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Projeto")
        verbose_name_plural = ("Projetos")

    nome = models.CharField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

class Habilidade(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Habilidade")
        verbose_name_plural = ("Habilidades")

    nome = models.CharField(max_length=255)

class MaturidadeProfissional(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Maturidade profissional")
        verbose_name_plural = ("Maturidades profissionais")

    nome = models.CharField(max_length=255)

class MaturidadeAcademica(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['id']
        verbose_name = ("Maturidade acadêmica")
        verbose_name_plural = ("Maturidades acadêmica")

    nome = models.CharField(max_length=255)

class Premio(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Prêmio")
        verbose_name_plural = ("Prêmios")

    nome = models.CharField(max_length=255)

class Profissional(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Profissional")
        verbose_name_plural = ("Profissionais")

    nome = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255)
    maturidade_profissional = models.ForeignKey(MaturidadeProfissional, related_name='maturidades_profissionais', on_delete=models.CASCADE)
    maturidade_academica = models.ForeignKey(MaturidadeAcademica, on_delete=models.CASCADE)
    cultura = models.ForeignKey(Cultura,  related_name='culturas', on_delete=models.CASCADE)
    areas_atuacao = models.ManyToManyField(AreaAtuacao)
    habilidades = models.ManyToManyField(Habilidade, blank=True)
    startups = models.ManyToManyField(Startup, blank=True)
    projetos = models.ManyToManyField(Projeto, blank=True)
    premios = models.ManyToManyField(Premio, blank=True)

class RecomendacaoHabilidades(models.Model):

    def __str__(self):
        return '{} -> {}'.format(self.recomendador, self.recomendado)

    class Meta:
        verbose_name = ("Recomendação de habilidade")
        verbose_name_plural = ("Recomendações de habilidades")

    recomendador = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='profissional_recomendador')
    recomendado = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidade)

class Vaga(models.Model):

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = ("Vaga")
        verbose_name_plural = ("Vagas")

    titulo = models.CharField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidade)
    maturidade_academica = models.ForeignKey(MaturidadeAcademica, on_delete=models.CASCADE)
    maturidade_profissional = models.ForeignKey(MaturidadeProfissional, on_delete=models.CASCADE)
    areas_atuacao = models.ManyToManyField(AreaAtuacao)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

class NPS(models.Model):

    def __str__(self):
        return str(self.nota)

    class Meta:
        verbose_name = ("Nota")
        verbose_name_plural = ("Nota")

    vaga = models.ForeignKey(Vaga, on_delete=models.DO_NOTHING)
    nota = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(0)])
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)