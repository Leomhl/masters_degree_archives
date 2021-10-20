from django.shortcuts import render
from core.models import Profissional, Vaga

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def recommendations(request):
    vagas = Vaga.objects.values('id','titulo')
    print(vagas)
    return render(request, 'recommendations.html', {'vagas': vagas})

def professionals(request):
    profissionais = list(Profissional.objects.values('nome', 'linkedin_url'))
    return render(request, 'professionals.html', {'profissionais': profissionais})

# Rotas para criar

# Rotas admin - OK
# Rota da rede social toda - ok
# Rota de about - ok
# Rota da tela de buscar candidato através da vaga (selecionar uma vaga e rodar) - ok