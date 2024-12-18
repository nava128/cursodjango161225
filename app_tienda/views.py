from django.shortcuts import render
from .models import *

def inicio(request):
	pedidos= Pedido.objects.all()
	clientes= Cliente.objects.all()

	total_clientes= clientes.count()
	total_pedidos= pedidos.count()

	entregados= pedidos.filter(estado='Entregado').count()
	pendientes= pedidos.filter(estado='Pendiente').count()
    
	context = {'pedidos':pedidos,'clientes':clientes,
	'total_pedidos':total_pedidos,	'entregados':entregados,
	'pendientes':pendientes}

	return render(request, 'app_tienda/inicio.html', context)

	

def productos(request):
	productos= Producto.objects.all()
	context = {'productos':productos}
	return render(request, 'app_tienda/productos.html', context)

def pedidos(request):
	return render(request, 'app_tienda/productos.html')

def clientes(request):
	return render(request, 'app_tienda/clientes.html')
