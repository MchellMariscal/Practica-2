# Simulador del Algoritmo de Dijkstra en consola
import heapq  # Librería para usar una cola de prioridad (mínimo primero)

# Función que implementa el algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    # Inicializa las distancias a todos los nodos como infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0  # La distancia del nodo inicial a sí mismo es 0

    visitados = set()  # Para llevar registro de los nodos ya procesados
    cola = [(0, inicio)]  # Cola de prioridad: (distancia, nodo)
    paso = 1  # Contador de pasos para mostrar en consola

    while cola:
        # Extrae el nodo con menor distancia conocida
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue  # Si ya fue visitado, lo salta

        print(f"Paso {paso}: Nodo actual: {nodo_actual}, Distancia: {distancia_actual}")
        paso += 1
        visitados.add(nodo_actual)

        # Recorre los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in visitados:
                nueva_distancia = distancia_actual + peso
                # Si se encuentra un camino más corto, se actualiza
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola, (nueva_distancia, vecino))
                    print(f"  Se actualiza la distancia de {vecino} a {nueva_distancia}")

    # Muestra las distancias finales desde el nodo inicial
    print("\nDistancias finales desde", inicio)
    for nodo, distancia in distancias.items():
        print(f"  {nodo}: {distancia}")

# Grafo de ejemplo representado como diccionario
# Cada nodo tiene vecinos con sus respectivos pesos (costos)
grafo = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 5, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

# Llama a la función con el nodo de inicio 'A'
dijkstra(grafo, 'A')
