from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
def vista_principal(request):
    return render(request, 'mantenedor/vista.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'mantenedor/lista.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'mantenedor/agregar.html', {'form': form})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')