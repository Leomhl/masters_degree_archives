from django.http import JsonResponse
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


# Core route of the application
def recommendationsapi(request):
    # seguir daqui
    profissionais = list(Profissional.objects.select_related('cultura', 'maturidade_academica', 'maturidade_profissional').values())
    print(profissionais)
    return JsonResponse(profissionais, safe=False)