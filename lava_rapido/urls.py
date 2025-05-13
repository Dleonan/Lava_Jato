from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inicio/', include('inicio.urls')),
    path('servicos/', include('servicos.urls')),
    path('clientes/', include('clientes.urls')),
    path('vendas/', include('vendas.urls')),    
    path('agendamentos/', include('agendamentos.urls')),
    path('estatisticas/', include('estatisticas.urls')),

    # Admin
    path('admin/', admin.site.urls),
]
