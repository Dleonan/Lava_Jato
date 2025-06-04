import json
from datetime import date
from django.shortcuts import render
from django.db.models import Count
from agendamentos.models import Agendamento

# cores e ordem fixa de cada status
STATUS_CONFIG = [
    ('Aguardando',  'rgba(255, 159, 64, 0.2)',  'rgba(255, 159, 64, 1)'),
    ('Em Lavagem',  'rgba(255,  99, 132, 0.2)',  'rgba(255,  99, 132, 1)'),
    ('Finalizado',  'rgba( 54, 162, 235, 0.2)',  'rgba( 54, 162, 235, 1)'),
]

def _build_dataset(qs, labels):
    """Monta e retorna o dataset do gráfico do Chart.js mantendo a ordem dos status"""
    stats = { item['status']: item['count'] for item in qs }
    data_list = []
    bg_list   = []
    br_list   = []
    for status, bg, br in STATUS_CONFIG:
        data_list.append(stats.get(status, 0))
        bg_list.append(bg)
        br_list.append(br)
    return {
        'labels': labels,
        'datasets': [{
            'label': 'Aguardando',
            'data': [ stats.get('Aguardando',0) ],
            'backgroundColor': STATUS_CONFIG[0][1],
            'borderColor':    STATUS_CONFIG[0][2],
            'borderWidth': 1,
            'barThickness': 20
        }, {
            'label': 'Em Lavagem',
            'data': [ stats.get('Em Lavagem',0) ],
            'backgroundColor': STATUS_CONFIG[1][1],
            'borderColor':    STATUS_CONFIG[1][2],
            'borderWidth': 1,
            'barThickness': 20
        }, {
            'label': 'Finalizado',
            'data': [ stats.get('Finalizado',0) ],
            'backgroundColor': STATUS_CONFIG[2][1],
            'borderColor':    STATUS_CONFIG[2][2],
            'borderWidth': 1,
            'barThickness': 20
        }]
    }

def estatisticas_diarias(request):
    hoje = date.today()
    qs = (
        Agendamento.objects
        .filter(data=hoje)
        .values('status')
        .annotate(count=Count('id'))
    )
    grafico_diario = _build_dataset(qs, [hoje.strftime('%d/%m/%Y')])
    return render(request, 'estatisticas/estatisticas_diarias.html', {
        'grafico_diario_json': json.dumps(grafico_diario)
    })

def estatisticas_mensais(request):
    hoje = date.today()
    # pega somente os agendamentos finalizados deste mês
    total_finalizado = (
        Agendamento.objects
        .filter(data__year=hoje.year, data__month=hoje.month, status='Finalizado')
        .count()
    )

    # monta o JSON com UM único dataset: “Finalizado”
    grafico_mensal = {
        'labels': [hoje.strftime('%B')],  # ex: ["maio"]
        'datasets': [{
            'label': 'Finalizado',
            'data': [total_finalizado],
            'backgroundColor': STATUS_CONFIG[2][1],
            'borderColor':    STATUS_CONFIG[2][2],
            'borderWidth': 1,
            'barThickness': 20,
        }]
    }

    return render(request, 'estatisticas/estatisticas_mensais.html', {
        'grafico_mensal_json': json.dumps(grafico_mensal)
    })