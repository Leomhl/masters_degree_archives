# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth import logout

# from .models import Receita

def index(request):
    # A rede social completa vai ficar nessa parte aqui

    # receitas = Receita.objects.all()
    #
    # dados = {
    #     'receitas': receitas
    # }

    return render(request, 'index.html')

# def receita(request, receita_id):
    # receita = get_object_or_404(Receita, pk=receita_id)
    #
    # dados = {
    #     'receita': receita
    # }

    # return render(request, 'receita.html', dados)

# Acho q n rola
# @login_required
# def logout(request):
#     logout(request)
    # return HttpResponseRedirect('admin')


# Rotas para criar
# Rotas admin - OK
# Rota da rede social toda
# Rota da tela de buscar candidato através da vaga (cadastrar ou selecionar uma vaga?)
# Rota da tela de pessoa recomendada