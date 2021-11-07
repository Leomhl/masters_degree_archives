from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
import json
from core.models import *
from core.common import helpers


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def recommendations(request):
    vagas = Vaga.objects.values('id','titulo')
    return render(request, 'recommendations.html', {'vagas': vagas})

def professionals(request):
    profissionais = list(Profissional.objects.values('nome', 'linkedin_url'))
    return render(request, 'professionals.html', {'profissionais': profissionais})


# Core of recommendations algorithm
def recommendationsapi(request):

    # Primeira função
    # 1 Ver o agrupamento na rede de um candidato para um profissional setado na vaga
    # 2 áreas de atuação do profissional e área da vaga e se são similares - ok
    # 3 popularidade na rede, o quanto o indivíduo está conectado com ela

    # Segunda função
    # 1 Maturidade profissional do candidato bater com a da vaga - ok
    # 2 Maturidade acadêmica do candidato bater com a da vaga - ok
    # 3 Número de premiações - ok
    # 4 Número de habilidades - ok
    # 5 Adaptação de cultura - ok
    # 6 Recomendação de habilidades - ok

    # Dados da vaga
    vaga = Vaga.objects.filter(id=request.GET['id'])
    tmpJson = serializers.serialize("json", vaga)
    vaga = json.loads(tmpJson)
    vaga[0]['fields']['id'] = vaga[0]['pk']
    vaga = vaga[0]['fields']

    # Dados do profissional
    profissionais = Profissional.objects.all()
    tmpJson = serializers.serialize("json", profissionais)
    profissionais = json.loads(tmpJson)

    # Dados das recomendacoes de habilidades
    recomendacoes_habilidades = RecomendacaoHabilidades.objects.all()
    tmpJson = serializers.serialize("json", recomendacoes_habilidades)
    recomendacoes_habilidades = json.loads(tmpJson)


    # Dados das maturidades acadêmicas
    mat_academica_temp = MaturidadeAcademica.objects.all()
    tmpJson = serializers.serialize("json", mat_academica_temp)
    mat_academica_temp = json.loads(tmpJson)
    mat_academica = {};

    for mat_acad in mat_academica_temp:
        mat_academica[mat_acad['pk']] = mat_acad['fields'];

    # Dados das maturidades profissionais
    mat_profissional_temp = MaturidadeProfissional.objects.all()
    tmpJson = serializers.serialize("json", mat_profissional_temp)
    mat_profissional_temp = json.loads(tmpJson)
    mat_profissional = {};

    for mat_prof in mat_profissional_temp:
        mat_profissional[mat_prof['pk']] = mat_prof['fields'];

    # Variável que servirá de retornor para a API
    recomendacao_resultado = []
    pontuacao = []

    # Inserção das recomendações no objeto do profissional
    for profissional in profissionais:
        profissional['fields']['id'] = profissional['pk']
        profissional = profissional['fields']

        for recomendacao_habilidade in recomendacoes_habilidades:
            if(recomendacao_habilidade['fields']['recomendado'] == profissional['id']):
                profissional['recomendacoes'] = recomendacao_habilidade['fields']['habilidades']
            else:
                profissional['recomendacoes'] = []

    # Função do coeficiente de competência

        peso_mat_prof = 0
        peso_mat_acad = 0
        peso_areas_similares = 0
        peso_habilidades = 0

        # Maturidade profissional
        if(profissional['maturidade_profissional'] == vaga['maturidade_profissional']):
            peso_mat_prof = 4
        elif(profissional['maturidade_profissional'] > vaga['maturidade_profissional']):
            peso_mat_prof = 2
        else:
            peso_mat_prof = 1


        # Maturidade acadêmica correta para a vaga
        if(profissional['maturidade_academica'] == vaga['maturidade_academica']):
            peso_mat_acad = 4

        # Testa se a maturidade é a mais baixa (1), não faz sentido recomendar um pós graduado pra uma vaga de jr
        elif(vaga['maturidade_academica'] == 1):
            if(profissional['maturidade_academica'] == 2):
                peso_mat_acad = 3
            elif(profissional['maturidade_academica'] != 1 and profissional['maturidade_academica'] != 2):
                peso_mat_acad = 0

        # Testa se a maturidade é a mais alta (5), não faz sentido recomendar um graduado pra uma vaga de referênca/doutor
        elif(vaga['maturidade_academica'] == 5):
            if(profissional['maturidade_academica'] == 4):
                peso_mat_acad = 3
            elif(profissional['maturidade_academica'] != 5 and profissional['maturidade_academica'] != 4):
                peso_mat_acad = 0

        # Caso a maturidade da vaga seja 2
        elif(vaga['maturidade_academica'] == 2):
            if(profissional['maturidade_academica'] == 1):
                peso_mat_acad = 1
            elif(profissional['maturidade_academica'] == 3):
                peso_mat_acad = 3
            elif(profissional['maturidade_academica'] == 4):
                peso_mat_acad = 2
            elif(profissional['maturidade_academica'] == 5):
                peso_mat_acad = 0

        # Caso a maturidade da vaga seja 3
        elif(vaga['maturidade_academica'] == 3):
            if(profissional['maturidade_academica'] == 1):
                peso_mat_acad = 0
            elif (profissional['maturidade_academica'] == 2):
                peso_mat_acad = 1
            elif(profissional['maturidade_academica'] == 4):
                peso_mat_acad = 3
            elif (profissional['maturidade_academica'] == 5):
                peso_mat_acad = 2

        # Caso a maturidade da vaga seja 4
        elif(vaga['maturidade_academica'] == 4):
            if(profissional['maturidade_academica'] == 5):
                peso_mat_acad = 3
            elif(profissional['maturidade_academica'] == 3):
                peso_mat_acad = 2
            elif(profissional['maturidade_academica'] == 1 or profissional['maturidade_academica'] == 2):
                peso_mat_acad = 0


        # Áreas de atuação similares
        for vaga_area in vaga['areas_atuacao']:
            for profissional_area in profissional['areas_atuacao']:
                if(vaga_area == profissional_area):
                    peso_areas_similares += 1

        for vaga_habilidade in vaga['habilidades']:
            for profissional_habilidade in profissional['habilidades']:
                if(vaga_habilidade == profissional_habilidade):
                    peso_habilidades += 1

        # Adaptação de cultura
        if(profissional['cultura'] == vaga['cultura']):
            peso_cultura = 4
        elif(profissional['cultura'] > vaga['cultura']):
            peso_cultura = 2
        else:
            peso_cultura = 1

        profissionalManaData = {
            'nome': profissional['nome'],
            'id': profissional['id'],
            'linkedin_url': profissional['linkedin_url'],
            'maturidade_academica': profissional['maturidade_academica'],
            'maturidade_profissional': profissional['maturidade_profissional'],

            'peso_mat_prof': peso_mat_prof,
            'peso_mat_acad': peso_mat_acad,
            'peso_premiacoes': len(profissional['premios']),
            'peso_areas_similares': peso_areas_similares,
            'peso_habilidades': peso_habilidades,
            'peso_cultura': peso_cultura,
            'peso_rec_habilidades': len(profissional['recomendacoes'])
        }


        # Após criar a outra função, utilizar a ordenação com base nos pesos
        pontuacao.append(profissionalManaData)
        # print('{}'.format(profissionalManaData))

    # recomendacao_resultado
    obj = {
        'profissionais': profissionais,
        'vaga': vaga,
    }

    # Retorno da API

    for candidato in pontuacao:
        total = candidato['peso_mat_prof'] + candidato['peso_mat_acad'] + candidato['peso_premiacoes'] + candidato['peso_rec_habilidades']
        total += candidato['peso_areas_similares'] + candidato['peso_habilidades'] + candidato['peso_cultura']

        recomendacao_resultado.append({
            'id': candidato['id'],
            'nome': candidato['nome'],
            'linkedin_url': candidato['linkedin_url'],
            'total': total,
            'maturidade_academica': mat_academica[candidato['maturidade_academica']]['nome'],
            'maturidade_profissional': mat_profissional[candidato['maturidade_profissional']]['nome']
        })

    helpers.quick_sort(recomendacao_resultado, 0, len(recomendacao_resultado) - 1, lambda x, y: x['total'] < y['total'])

    return JsonResponse(recomendacao_resultado, safe=False)