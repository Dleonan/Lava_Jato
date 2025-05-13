from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_servicos, name='listar_servicos'),
    path('editar/<int:servico_id>/', views.editar_servico, name='editar_servico'),
    path('excluir/<int:servico_id>/', views.excluir_servico, name='excluir_servico'),
]