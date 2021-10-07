from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def recommendations(request):
    return render(request, 'recommendations.html')


# Rotas para criar

# Rotas admin - OK
# Rota da rede social toda - ok
# Rota de about - ok
# Rota da tela de buscar candidato através da vaga (selecionar uma vaga e rodar) - ok