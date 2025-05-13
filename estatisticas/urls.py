# estatisticas/urls.py

from django.urls import path
from .views import estatisticas_diarias, estatisticas_mensais

urlpatterns = [
    path('diarias/', estatisticas_diarias, name='estatisticas_diarias'),
    path('mensais/', estatisticas_mensais, name='estatisticas_mensais'),
]
