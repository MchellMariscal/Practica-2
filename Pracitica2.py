import time
import copy

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

def mostrar_productos(lista):
    for producto in lista:
        print(producto)
    print()