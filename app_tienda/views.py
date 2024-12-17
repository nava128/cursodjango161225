from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
	return HttpResponse('Inicio')

def productos(request):
	return HttpResponse('productos')

def clientes(request):
	return HttpResponse('clientes')