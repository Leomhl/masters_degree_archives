from django.contrib import admin
from .models import *

admin.site.register(Profissional)
admin.site.register(AreaAtuacao)
admin.site.register(Habilidade)
admin.site.register(Startup)
admin.site.register(Projeto)
admin.site.register(Premio)


admin.site.site_header = 'Maná admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Maná'
