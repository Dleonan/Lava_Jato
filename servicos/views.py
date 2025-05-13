from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Servico

def listar_servicos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        if nome and valor:
            Servico.objects.create(nome=nome, valor=valor)
        return redirect('listar_servicos')

    servicos = Servico.objects.all()
    return render(request, 'servicos/listar.html', {'servicos': servicos})

def editar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    if request.method == 'POST':
        servico.nome = request.POST.get('nome')
        servico.valor = request.POST.get('valor')
        servico.save()
        return redirect('listar_servicos')

    return render(request, 'servicos/editar.html', {'servico': servico})

@require_POST
def excluir_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    servico.delete()
    return redirect('listar_servicos')