from django.db import models
from datetime import datetime

class Cultura(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Cultura")
        verbose_name_plural = ("Culturas")

    nome = models.CharField(max_length=255)

class Setor(models.Model):
    def __str__(self):
        return self.nome + " - "  + self.descricao

    class Meta:
        verbose_name_plural = ("Setores")

    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

class Startup(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Startup")
        verbose_name_plural = ("Startups")

    nome = models.CharField(max_length=255)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)


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

class AreaAtuacao(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Área de atuação")
        verbose_name_plural = ("Áreas de atuação")

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
        ordering = ['nome']
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
    maturidade_profissional = models.ForeignKey(MaturidadeProfissional, on_delete=models.CASCADE)
    maturidade_academica = models.ForeignKey(MaturidadeAcademica, on_delete=models.CASCADE)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    areas_atuacao = models.ManyToManyField(AreaAtuacao)
    habilidades = models.ManyToManyField(Habilidade)
    projetos = models.ManyToManyField(Projeto)
    premios = models.ManyToManyField(Premio)

class RecomendacaoProfissional(models.Model):
    class Meta:
        verbose_name = ("Recomendação profissional")
        verbose_name_plural = ("Recomendações profissionais")

    recomendador = models.ForeignKey(Profissional, on_delete=models.CASCADE, related_name='profissional_recomendador')
    recomendado = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)

class Vaga(models.Model):

    titulo = models.CharField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidade)
    maturidade_academica = models.ForeignKey(MaturidadeAcademica, on_delete=models.CASCADE)
    maturidade_profissional = models.ForeignKey(MaturidadeProfissional, on_delete=models.CASCADE)
    areas_atuacao = models.ManyToManyField(AreaAtuacao)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)

