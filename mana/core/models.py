from django.db import models
from datetime import datetime

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

class Cultura(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Cultura")
        verbose_name_plural = ("Culturas")

    nome = models.CharField(max_length=255)

class Profissional(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Profissional")
        verbose_name_plural = ("Profissionais")

    nome = models.CharField(max_length=255)
    maturidade_profissional = models.ForeignKey(MaturidadeProfissional, on_delete=models.RESTRICT)
    maturidade_academica = models.ForeignKey(MaturidadeAcademica, on_delete=models.RESTRICT)
    cultura = models.ForeignKey(Cultura, on_delete=models.RESTRICT)

class AreaAtuacao(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Área de atuação")
        verbose_name_plural = ("Áreas de atuação")

    nome = models.CharField(max_length=255)
#
# class ProfissionalAreaAtuacao(models.Model):
#
#     class Meta:
#         verbose_name = ("Área de atuação")
#         verbose_name_plural = ("Áreas de atuação")
#
#     profissional = models.ForeignKey(Profissional, on_delete=models.RESTRICT)
#     area_atuacao = models.ForeignKey(AreaAtuacao, on_delete=models.RESTRICT)

class Habilidade(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Habilidade")
        verbose_name_plural = ("Habilidades")

    nome = models.CharField(max_length=255)

# class ProfissionalHabilidade(models.Model):
#
#     class Meta:
#         verbose_name = ("Profissional Habilidade")
#         verbose_name_plural = ("Profissionais Habilidades")
#
#     profissional = models.ForeignKey(Profissional, on_delete=models.RESTRICT)
#     habilidade = models.ForeignKey(Habilidade, on_delete=models.RESTRICT)

class Startup(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Startup")
        verbose_name_plural = ("Startups")

    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    criado_em = models.DateTimeField(default=datetime.now(), blank=True)

class Projeto(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Projeto")
        verbose_name_plural = ("Projetos")

    nome = models.CharField(max_length=255)
    startup = models.ForeignKey(Startup, on_delete=models.RESTRICT)

class Premio(models.Model):
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = ("Prêmio")
        verbose_name_plural = ("Prêmios")

    nome = models.CharField(max_length=255)


# class ProfissionalProjeto(models.Model):
#
#     class Meta:
#         verbose_name = ("Profissional Projeto")
#         verbose_name_plural = ("Profissionais Projetos")
#
#     profissional = models.ForeignKey(Profissional, on_delete=models.RESTRICT)
#     projeto = models.ForeignKey(Projeto, on_delete=models.RESTRICT)