from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Cliente

def listar_clientes(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        veiculo = request.POST.get("veiculo")
        modelo = request.POST.get("modelo")
        cor = request.POST.get("cor")
        placa = request.POST.get("placa")

        Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            veiculo=veiculo,
            modelo=modelo,
            cor=cor,
            placa=placa
        )
        return redirect("listar_clientes")

    clientes = Cliente.objects.all()
    return render(request, "clientes/listar.html", {"clientes": clientes})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        cliente.nome = request.POST.get("nome")
        cliente.telefone = request.POST.get("telefone")
        cliente.veiculo = request.POST.get("veiculo")
        cliente.modelo = request.POST.get("modelo")
        cliente.cor = request.POST.get("cor")
        cliente.placa = request.POST.get("placa")
        cliente.save()
        return redirect("listar_clientes")

    return render(request, "clientes/editar.html", {"cliente": cliente})

@require_POST
def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect("listar_clientes")
