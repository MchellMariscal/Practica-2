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

def ordenar_insercion(productos):
    for i in range(1, len(productos)):
        clave = productos[i]
        j = i - 1
        while j >= 0 and productos[j].precio > clave.precio:
            productos[j + 1] = productos[j]
            j -= 1
        productos[j + 1] = clave

def quicksort(productos):
    if len(productos) <= 1:
        return productos
    pivote = productos[-1]
    menores = [p for p in productos[:-1] if p.precio < pivote.precio]
    mayores = [p for p in productos[:-1] if p.precio >= pivote.precio]
    return quicksort(menores) + [pivote] + quicksort(mayores)

def ejecutar_ordenamiento(nombre, funcion, productos):
    copia = copy.deepcopy(productos)
    print(f"\n--- Ordenamiento {nombre} por precio ---")
    print("Productos originales:")
    mostrar_productos(copia)

    inicio = time.time()
    if nombre == "QuickSort":
        copia = funcion(copia)  # QuickSort devuelve una nueva lista
    else:
        funcion(copia)          # Otros modifican la lista en el lugar
    fin = time.time()

    print("Productos ordenados:")
    mostrar_productos(copia)
    print(f"Tiempo: {(fin - inicio) * 1000:.2f} ms")

def main():
    productos = []

    cantidad = int(input("¿Cuántos productos deseas ingresar?: "))
    for i in range(cantidad):
        nombre = input(f"\nNombre del producto {i + 1}: ")
        precio = float(input(f"Precio del producto {i + 1}: $"))
        productos.append(Producto(nombre, precio))

    ejecutar_ordenamiento("Burbuja", ordenar_burbuja, productos)
    ejecutar_ordenamiento("Selección", ordenar_seleccion, productos)
    ejecutar_ordenamiento("Inserción", ordenar_insercion, productos)
    ejecutar_ordenamiento("QuickSort", quicksort, productos)

if __name__ == "__main__":
    main()
