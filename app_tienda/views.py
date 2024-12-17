from django.shortcuts import render


def inicio(request):
	return render(request, 'app_tienda/inicio.html')

def productos(request):
	return render(request, 'app_tienda/productos.html')

def clientes(request):
	return render(request, 'app_tienda/clientes.html')
