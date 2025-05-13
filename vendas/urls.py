
from django.urls import path
from . import views
from .views import abrir_caixa, registrar_venda, fechar_caixa, resumo_caixa

urlpatterns = [
    path('abrir-caixa/', views.abrir_caixa, name='abrir_caixa'),
    path('registrar-venda/', views.registrar_venda, name='registrar_venda'),
    path('fechar-caixa/', views.fechar_caixa, name='fechar_caixa'),
    path('resumo/', resumo_caixa, name='resumo_caixa'),
]
