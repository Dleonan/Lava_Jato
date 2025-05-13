from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from clientes.models import Cliente
from servicos.models import Servico
from django.contrib import messages

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('data', 'hora')
    return render(request, 'agendamentos/listar.html', {'agendamentos': agendamentos})

def novo_agendamento(request):
    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        observacoes = request.POST.get('observacoes')
        status = request.POST.get('status')  # Capturando o status

        Agendamento.objects.create(
            cliente_id=cliente_id,
            servico_id=servico_id,
            data=data,
            hora=hora,
            observacoes=observacoes,
            status=status  # Salvando o status
        )
        messages.success(request, 'Agendamento criado com sucesso.')
        return redirect('listar_agendamentos')

    return render(request, 'agendamentos/novo.html', {
        'clientes': clientes,
        'servicos': servicos
    })

def alterar_status(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == 'POST':
        if agendamento.status == 'Finalizado':
            messages.warning(request, 'Este agendamento já foi finalizado e não pode mais ser alterado.')
            return redirect('listar_agendamentos')

        novo_status = request.POST.get('status')
        agendamento.status = novo_status
        agendamento.save()

        messages.success(request, f'O status do agendamento foi alterado para {novo_status}.')
        return redirect('listar_agendamentos')

    return redirect('listar_agendamentos')
