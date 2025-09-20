from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Cliente
from .forms import ClienteForm, RegistroForm
from django.contrib.auth import login
from django.core.paginator import Paginator


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após registro
            return redirect('lista_clientes')
    else:
        form = RegistroForm()
    return render(request, 'clientes/registro.html', {'form': form})


@login_required
def lista_clientes(request):
    clientes_lista = Cliente.objects.filter(usuario=request.user).order_by('nome')  # ordenar por nome
    paginator = Paginator(clientes_lista, 10)  # 10 clientes por página

    page_number = request.GET.get('page')  # número da página vindo da URL ?page=1,2,...
    page_obj = paginator.get_page(page_number)  # obtém a página solicitada

    return render(request, 'clientes/lista_clientes.html', {'page_obj': page_obj})

@login_required
def cria_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, usuario=request.user)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(usuario=request.user)
    return render(request, 'clientes/form_cliente.html', {'form': form})


@login_required
def edita_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk, usuario=request.user)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente, usuario=request.user)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente, usuario=request.user)
    return render(request, 'clientes/form_cliente.html', {'form': form})

@login_required
def deleta_cliente(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk, usuario=request.user)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não encontrado")

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/confirma_delete.html', {'cliente': cliente})
