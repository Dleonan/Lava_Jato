
from django.contrib import admin
from .models import Caixa, Venda, ItemVenda, FormaPagamento

@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aberto', 'aberto_em', 'fechado_em', 'valor_inicial', 'valor_final')
    list_filter = ('aberto',)
    readonly_fields = ('aberto_em', 'fechado_em')

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'caixa', 'forma_pagamento', 'data_hora')
    list_filter = ('forma_pagamento', 'caixa')
    inlines = [ItemVendaInline]