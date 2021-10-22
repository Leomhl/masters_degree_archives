from django.urls import path
from . import views

from django.urls import include, path
from rest_framework import routers
from core.api.viewset import RecomendacoesViewSet

router = routers.DefaultRouter()
router.register(r'recomendacoes', RecomendacoesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('professionals', views.professionals, name='professionals'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

