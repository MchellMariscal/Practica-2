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

    def ordenar_burbuja(productos):
    n = len(productos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if productos[j].precio > productos[j + 1].precio:
                productos[j], productos[j + 1] = productos[j + 1], productos[j]

                def ordenar_seleccion(productos):
    n = len(productos)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if productos[j].precio < productos[min_idx].precio:
                min_idx = j
        productos[i], productos[min_idx] = productos[min_idx], productos[i]