from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
import json
from core.models import *

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


# Core route of the application
def recommendationsapi(request):

    # Primeira função
    # 1 Ver o agrupamento na rede de um candidato para um profissional setado na vaga
    # 2 áreas de atuação do profissional e área da vaga e se são similares - ok
    # 3 popularidade na rede, o quanto o indivíduo está conectado com ela

    # Segunda função
    # 1 Maturidade profissional do candidato bater com a da vaga - ok
    # 2 Maturidade acadêmica do candidato bater com a da vaga - ok
    # 3 Número de premiações - ok
    # 4 Adaptação de cultura - ok

    # profissionais = Profissional.objects.values()
    # culturas = Cultura.objects.values()


    # {
    # id: 123, #id do profissional,
    # areas_similares: 1, #quantidade de áreas que são similares a da vaga
    # numero_premiacoes: 2, #quantidade de prêmios que tem
    # maturidade_acadêmica: true, #se tem ou não a maturidade exigida
    # maturidade_profissional: true, #se tem ou não a maturidade exigida
    # adaptacao_cultura: true, #se ele se adapta ou não,
    # agrupamento: 123, #a definir,
    # popularidade: 123, #o quão conectado a outros nós o profissional está
    # }


    profissionais = Profissional.objects.all()
    tmpJson = serializers.serialize("json", profissionais)
    tmpObj = json.loads(tmpJson)

    return JsonResponse(tmpObj, safe=False)