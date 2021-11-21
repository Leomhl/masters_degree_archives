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
    vagas = Vaga.objects.values('id', 'titulo')
    return render(request, 'recommendations.html', {'vagas': vagas})

def professionals(request):
    profissionais = list(Profissional.objects.values('nome', 'linkedin_url'))
    return render(request, 'professionals.html', {'profissionais': profissionais})


def relatorio_nps(request):
    npss = list(NPS.objects.values('vaga', 'nota'))
    vagas = list(Vaga.objects.values('id', 'titulo'))

    for vaga in vagas:
        vaga['detratores'] = 0
        vaga['promotores'] = 0
        vaga['nps'] = 0

        for nps in npss:
            if nps['vaga'] == vaga['id']:

                if nps['nota'] <= 6:
                    vaga['detratores'] += nps['vaga']

                if nps['nota'] >= 9:
                    vaga['promotores'] += nps['vaga']

        vaga['nps'] = (vaga['promotores'] - vaga['detratores']) * 100

    return render(request, 'relatorio_nps.html', {'vagas': vagas})


# Core of recommendations algorithm
def recommendationsapi(request):
    # Dados gerais para o cálculo de popularidade
    areas_total = AreaAtuacao.objects.count()
    habilidades_total = Habilidade.objects.count()
    projetos_total = Projeto.objects.count()
    premios_total = Premio.objects.count()
    endossos_total = RecomendacaoHabilidades.objects.count()

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

    # Dados dos endossos
    recomendacoes_habilidades = RecomendacaoHabilidades.objects.all()
    tmpJson = serializers.serialize("json", recomendacoes_habilidades)
    recomendacoes_habilidades = json.loads(tmpJson)

    # Dados das maturidades acadêmicas
    mat_academica_temp = MaturidadeAcademica.objects.all()
    tmpJson = serializers.serialize("json", mat_academica_temp)
    mat_academica_temp = json.loads(tmpJson)
    mat_academica = {}

    for mat_acad in mat_academica_temp:
        mat_academica[mat_acad['pk']] = mat_acad['fields']

    # Dados das maturidades profissionais
    mat_profissional_temp = MaturidadeProfissional.objects.all()
    tmpJson = serializers.serialize("json", mat_profissional_temp)
    mat_profissional_temp = json.loads(tmpJson)
    mat_profissional = {}

    for mat_prof in mat_profissional_temp:
        mat_profissional[mat_prof['pk']] = mat_prof['fields']

    # Variável que servirá de retornor para a API
    recomendacao_resultado = []
    pontuacao = []

    # Inserção das recomendações no objeto do profissional
    for profissional in profissionais:
        profissional['fields']['id'] = profissional['pk']
        profissional = profissional['fields']

        for recomendacao_habilidade in recomendacoes_habilidades:
            if recomendacao_habilidade['fields']['recomendado'] == profissional['id']:
                profissional['recomendacoes'] = recomendacao_habilidade['fields']['habilidades']
            else:
                profissional['recomendacoes'] = []

        # Função do coeficiente de competência
        peso_mat_prof = 0
        peso_mat_acad = 0
        peso_habilidades = 0

        if vaga['maturidade_profissional'] == profissional['maturidade_profissional']:
            peso_mat_prof = 50

        if vaga['maturidade_profissional'] == 1:
            if profissional['maturidade_profissional'] == 2:
                peso_mat_prof = -30
            elif profissional['maturidade_profissional'] == 3:
                peso_mat_prof = -50

        if vaga['maturidade_profissional'] == 2:
            if profissional['maturidade_profissional'] == 3:
                peso_mat_prof = -30
            elif profissional['maturidade_profissional'] == 1:
                peso_mat_prof = -50

        if (vaga['maturidade_profissional'] == 3):
            if profissional['maturidade_profissional'] == 2:
                peso_mat_prof = -30
            elif profissional['maturidade_profissional'] == 1:
                peso_mat_prof = -50

        # Maturidade acadêmica correta para a vaga
        if profissional['maturidade_academica'] == vaga['maturidade_academica']:
            peso_mat_acad = 50

        # Testa se a maturidade é a mais baixa (1), não faz sentido recomendar um pós graduado pra uma vaga de jr
        elif vaga['maturidade_academica'] == 1:
            if profissional['maturidade_academica'] == 2:
                peso_mat_acad = 25
            elif profissional['maturidade_academica'] != 1 and profissional['maturidade_academica'] != 2:
                peso_mat_acad = 0

        # Testa se a maturidade é a mais alta (5), não faz sentido recomendar um graduado pra uma vaga de referênca/doutor
        elif vaga['maturidade_academica'] == 5:
            if profissional['maturidade_academica'] == 4:
                peso_mat_acad = 25
            elif profissional['maturidade_academica'] != 5 and profissional['maturidade_academica'] != 4:
                peso_mat_acad = 0

        # Caso a maturidade da vaga seja 2
        elif vaga['maturidade_academica'] == 2:
            if profissional['maturidade_academica'] == 1:
                peso_mat_acad = 6.25
            elif profissional['maturidade_academica'] == 3:
                peso_mat_acad = 25
            elif profissional['maturidade_academica'] == 4:
                peso_mat_acad = 12.5
            elif profissional['maturidade_academica'] == 5:
                peso_mat_acad = 0

        # Caso a maturidade da vaga seja 3
        elif vaga['maturidade_academica'] == 3:
            if (profissional['maturidade_academica'] == 1):
                peso_mat_acad = 0
            elif profissional['maturidade_academica'] == 2:
                peso_mat_acad = 6.25
            elif profissional['maturidade_academica'] == 4:
                peso_mat_acad = 25
            elif profissional['maturidade_academica'] == 5:
                peso_mat_acad = 12.5

        # Caso a maturidade da vaga seja 4
        elif vaga['maturidade_academica'] == 4:
            if profissional['maturidade_academica'] == 5:
                peso_mat_acad = 25
            elif profissional['maturidade_academica'] == 3:
                peso_mat_acad = 12.5
            elif profissional['maturidade_academica'] == 1 or profissional['maturidade_academica'] == 2:
                peso_mat_acad = 0

        for vaga_habilidade in vaga['habilidades']:
            for profissional_habilidade in profissional['habilidades']:
                if (vaga_habilidade == profissional_habilidade):
                    peso_habilidades += 25

        # Adaptação de cultura
        if (profissional['cultura'] == vaga['cultura']):
            peso_cultura = 15
        elif (profissional['cultura'] > vaga['cultura']):
            peso_cultura = 10
        else:
            peso_cultura = 5

        # Função de conexão
        peso_areas_similares = 0
        peso_popularidade = 0
        grau_profissional = 0
        nos_da_rede = 100  # fazer um somatório de tudo

        # Áreas de atuação similares
        for vaga_area in vaga['areas_atuacao']:
            for profissional_area in profissional['areas_atuacao']:
                if (vaga_area == profissional_area):
                    peso_areas_similares += 10

        nos_da_rede = areas_total + habilidades_total + projetos_total + premios_total + endossos_total
        grau_profissional = len(profissional['recomendacoes']) + len(profissional['areas_atuacao']) + len(
            profissional['startups']) + len(profissional['projetos']) + len(profissional['premios'])

        if vaga['maturidade_profissional'] == 3:
            # Sênior
            peso_popularidade = (grau_profissional / (nos_da_rede - 1)) * 1000
        elif vaga['maturidade_profissional'] == 2:
            # Pleno
            peso_popularidade = (grau_profissional / (nos_da_rede - 1)) * 500
        else:
            # Júnior o peso precisa ser 0 para não tornar desleal a competição
            # já que obviamente ele não terá muita conexão com a rede
            peso_popularidade = 0

        profissionalManaData = {
            'nome': profissional['nome'],
            'id': profissional['id'],
            'linkedin_url': profissional['linkedin_url'],
            'maturidade_academica': profissional['maturidade_academica'],
            'maturidade_profissional': profissional['maturidade_profissional'],

            # Função de competência
            'peso_mat_prof': peso_mat_prof,
            'peso_mat_acad': peso_mat_acad,
            'peso_premiacoes': len(profissional['premios']),
            'peso_habilidades': peso_habilidades,
            'peso_cultura': peso_cultura,

            # Função de conexão
            'peso_areas_similares': peso_areas_similares,
            'peso_endosso': len(profissional['recomendacoes']) * 5,
            'peso_popularidade': peso_popularidade
        #     Tá faltando o profissional da vaga
        }

        # Após criar a outra função, utilizar a ordenação com base nos pesos
        pontuacao.append(profissionalManaData)

    # Retorno da API
    for candidato in pontuacao:
        total = candidato['peso_mat_prof'] + candidato['peso_mat_acad'] + candidato['peso_premiacoes'] + candidato[
            'peso_endosso']
        total += candidato['peso_areas_similares'] + candidato['peso_habilidades'] + candidato['peso_cultura'] + \
                 candidato['peso_popularidade']

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


def npsapi(request):
    try:
        nps = NPS(nota=request.POST['nota'], usuario=User.objects.filter(id=request.user.id).first(),
                  vaga=Vaga.objects.filter(id=request.POST['vaga_id']).first())
        nps.save()
        return JsonResponse({'status': 'ok'}, safe=False)
    except:
        return JsonResponse({'status': 'error'}, safe=False)
