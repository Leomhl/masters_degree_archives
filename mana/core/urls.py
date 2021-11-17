from . import views
from django.urls import path



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.recommendations, name='recommendations'),
    path('about', views.about, name='about'),
    path('professionals', views.professionals, name='professionals'),
    path('api/recomendacoes/', views.recommendationsapi, name="recommendations_api"),
    path('api/nps/', views.npsapi, name="nps_api"),
]

