from django.contrib import admin

# Register your models here.
from .models import Cliente, Producto, Pedido, Etiqueta

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Etiqueta)