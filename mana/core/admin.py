from django.contrib import admin
from .models import *

admin.site.register(MaturidadeProfissional)
admin.site.register(MaturidadeAcademica)
admin.site.register(Cultura)
admin.site.register(Profissional)
admin.site.register(AreaAtuacao)
admin.site.register(Habilidade)
admin.site.register(Startup)
admin.site.register(Projeto)
admin.site.register(Premio)
admin.site.register(RecomendacaoHabilidades)
admin.site.register(Vaga)

admin.site.site_header = 'Maná admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Maná'
