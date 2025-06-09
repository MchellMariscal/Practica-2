# Simulador del Algoritmo de Kruskal para Árbol de Expansión Mínima y Máxima

# Clase para representar un grafo con lista de aristas
class Grafo:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.aristas = []  # Lista de aristas (peso, u, v)

    # Agregar arista al grafo
    def agregar_arista(self, u, v, peso):
        self.aristas.append((peso, u, v))

    # Encontrar el subconjunto de un elemento i
    def encontrar(self, padre, i):
        if padre[i] != i:
            padre[i] = self.encontrar(padre, padre[i])
        return padre[i]

    # Unión de dos subconjuntos
    def unir(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)
        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    # Algoritmo de Kruskal (modo = 'min' para mínimo, 'max' para máximo)
    def kruskal(self, modo='min'):
        resultado = []  # Aristas del MST
        i = 0  # Índice para recorrer aristas
        e = 0  # Conteo de aristas incluidas

        # Ordenar aristas por peso (ascendente o descendente)
        self.aristas.sort(reverse=(modo == 'max'))

        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        print("\nPaso a paso del Árbol de {} costo (Kruskal):".format("Máximo" if modo == 'max' else "Mínimo"))

        while e < self.V - 1:
            peso, u, v = self.aristas[i]
            i += 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)

            if x != y:
                e += 1
                resultado.append((u, v, peso))
                self.unir(padre, rango, x, y)
                print(f"  Arista agregada: ({u}, {v}) con peso {peso}")
            else:
                print(f"  Arista descartada: ({u}, {v}) con peso {peso} (ciclo)")

        print("\nAristas en el Árbol de {} costo:".format("Máximo" if modo == 'max' else "Mínimo"))
        for u, v, peso in resultado:
            print(f"  ({u}, {v}) con peso {peso}")

# Crear un grafo de ejemplo con 4 nodos
n = 4
g = Grafo(n)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)

# Simular Kruskal para árbol de costo mínimo
g.kruskal(modo='min')

# Simular Kruskal para árbol de costo máximo
g.kruskal(modo='max')
