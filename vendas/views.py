from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Caixa, Venda, FormaPagamento, ItemVenda
from clientes.models import Cliente
from servicos.models import Servico
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder

def abrir_caixa(request):
    caixa_aberto = Caixa.objects.filter(aberto=True).last()
    if caixa_aberto:
        messages.info(request, 'Já existe um caixa aberto. Redirecionando para a tela de vendas.')
        return redirect('registrar_venda')

    if request.method == 'POST':
        valor_inicial = request.POST.get('valor_inicial')
        Caixa.objects.create(valor_inicial=valor_inicial)
        messages.success(request, 'Caixa aberto com sucesso.')
        return redirect('registrar_venda')

    return render(request, 'vendas/abrir_caixa.html')

def registrar_venda(request):
    caixa_aberto = Caixa.objects.filter(aberto=True).last()
    if not caixa_aberto:
        messages.warning(request, 'Não há caixa aberto. Abra um caixa primeiro.')
        return redirect('abrir_caixa')

    clientes = Cliente.objects.all()
    servicos = Servico.objects.all()
    formas_pagamento = FormaPagamento.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        forma_pagamento_id = request.POST.get('forma_pagamento')
        servico_id = request.POST.get('servico')
        valor = Decimal(request.POST.get('valor'))
        desconto = Decimal(request.POST.get('desconto', 0))

        valor_final = max(valor - desconto, Decimal('0'))

        venda = Venda.objects.create(
            cliente_id=cliente_id,
            caixa=caixa_aberto,
            forma_pagamento_id=forma_pagamento_id
        )

        ItemVenda.objects.create(
            venda=venda,
            servico_id=servico_id,
            valor=valor_final
        )

        messages.success(request, f'Venda registrada com sucesso. Valor final: R$ {valor_final:.2f}')
        return redirect('registrar_venda')

    servico_valores_json = json.dumps(
        {str(s.id): float(s.valor) for s in servicos},
        cls=DjangoJSONEncoder
    )

    return render(request, 'vendas/registrar_venda.html', {
        'clientes': clientes,
        'servicos': servicos,
        'formas_pagamento': formas_pagamento,
        'servico_valores_json': servico_valores_json
    })

def fechar_caixa(request):
    caixa_aberto = Caixa.objects.filter(aberto=True).last()
    if caixa_aberto:
        total_vendas = Venda.objects.filter(caixa=caixa_aberto)
        total = ItemVenda.objects.filter(venda__in=total_vendas).aggregate(Sum('valor'))['valor__sum'] or 0
        caixa_aberto.valor_final = total + caixa_aberto.valor_inicial
        caixa_aberto.fechado_em = timezone.now()
        caixa_aberto.aberto = False
        caixa_aberto.save()
        messages.success(request, 'Caixa fechado com sucesso.')
    else:
        messages.warning(request, 'Nenhum caixa aberto encontrado.')
    return redirect('abrir_caixa')


def resumo_caixa(request):
    caixa_aberto = Caixa.objects.filter(aberto=True).last()
    resumo = []
    total_geral = 0

    if caixa_aberto:
        resumo = ItemVenda.objects.filter(venda__caixa=caixa_aberto) \
            .values('venda__forma_pagamento__descricao') \
            .annotate(total=Sum('valor'))

        total_geral = ItemVenda.objects.filter(venda__caixa=caixa_aberto) \
            .aggregate(total=Sum('valor'))['total'] or 0
    else:
        messages.warning(request, 'Nenhum caixa aberto encontrado.')

    caixas_fechados = Caixa.objects.filter(aberto=False).order_by('-fechado_em')

    return render(request, 'vendas/resumo_caixa.html', {
        'resumo': resumo,
        'total_geral': total_geral,
        'caixa_aberto': caixa_aberto,
        'caixas_fechados': caixas_fechados
    })