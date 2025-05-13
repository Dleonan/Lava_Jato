from django.urls import path
from .views import listar_agendamentos, novo_agendamento, alterar_status


urlpatterns = [
    path('', listar_agendamentos, name='listar_agendamentos'),
    path('novo/', novo_agendamento, name='criar_agendamento'),
    path('alterar_status/<int:agendamento_id>/', alterar_status, name='alterar_status'),
]