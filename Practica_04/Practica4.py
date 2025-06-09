# Simulador del Algoritmo de Prim en consola (Árbol de Expansión Mínima)
import heapq

def prim(grafo, inicio):
    visitados = set()  # Para llevar registro de los nodos ya incluidos en el árbol
    arbol = []         # Guardará las aristas del árbol de expansión mínima
    cola = [(0, inicio, None)]  # Cola de prioridad: (peso, nodo_actual, nodo_origen)
    paso = 1

    while cola:
        peso, nodo, origen = heapq.heappop(cola)

        if nodo in visitados:
            continue

        visitados.add(nodo)
        if origen:
            arbol.append((origen, nodo, peso))
            print(f"Paso {paso}: Se agrega la arista ({origen} - {nodo}) con peso {peso}")
            paso += 1
        else:
            print(f"Paso {paso}: Nodo inicial {nodo} agregado al árbol")
            paso += 1

        for vecino, p in grafo[nodo].items():
            if vecino not in visitados:
                heapq.heappush(cola, (p, vecino, nodo))

    # Mostrar árbol mínimo resultante
    print("\nÁrbol de Expansión Mínima generado:")
    for origen, destino, peso in arbol:
        print(f"  {origen} - {destino}: {peso}")

# Grafo de ejemplo
# Representado como un diccionario de adyacencia con pesos
grafo = {
    'A': {'B': 3, 'D': 1},
    'B': {'A': 3, 'C': 1, 'D': 3},
    'C': {'B': 1, 'D': 1},
    'D': {'A': 1, 'B': 3, 'C': 1}
}

# Ejecutar el algoritmo desde el nodo 'A'
prim(grafo, 'A')
