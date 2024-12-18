from django.db import models

# Create your models here.

class Cliente(models.Model):
	nombre = models.CharField(max_length=200, null=True)
	telefono = models.CharField(max_length=200, null=True)
	correo = models.CharField(max_length=200, null=True)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return self.nombre

class Etiqueta(models.Model):
	nombre = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	CATEGORIA = (
			('Interior', 'Interior'),
			('Exterior', 'Exterior'),
			) 

	nombre = models.CharField(max_length=200, null=True)
	precio = models.FloatField(null=True)
	categoria = models.CharField(max_length=200, null=True, choices=CATEGORIA)
	descripcion = models.CharField(max_length=200, null=True)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.nombre


class Pedido(models.Model):
	ESTADO = (
			('Pendiente', 'Pendiente'),
			('En salida para entrega', 'En salida para entrega'),
			('Entregado', 'Entregado'),
			)

	#cliente = 
	Cliente = models.ForeignKey(Cliente, null=True, on_delete= models.SET_NULL)
	#producto = 
	Producto = models.ForeignKey(Producto, null=True, on_delete= models.SET_NULL)
	estado = models.CharField(max_length=200, null=True, choices=ESTADO)
	fecha_de_creacion = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return self.Producto.nombre
		

	