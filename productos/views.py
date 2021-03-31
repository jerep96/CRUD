from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .form import ProductForm
from .models import Product


# Create your views here.
@login_required()
def home(request):
    return redirect('productos:lista')


def lista(request, id_product=None):
    products = Product.objects.all()
    contexto = {
        'products': products
    }
    return render(request, 'lista_producto.html', contexto)


def crearProducto(request, id_product=None):
    products = None
    if id_product:
        products = Product.objects.get(id=id_product)
        form = ProductForm(instance=products)
        boton = 'Editar'
    else:
        form = ProductForm()
        boton = 'Cargar'
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('productos:lista')
    return render(request, 'crear_producto.html', {'form': form, 'boton': boton})


def eliminarProducto(request, id_product):
    products = Product.objects.get(id=id_product)
    eliminado = False
    products.delete()
    contexto = {
        eliminado: True
    }
    return redirect('productos:lista')
