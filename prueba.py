from collections import deque

class EstadoTriangulo:
    def __init__(self, nodos=None, disponibles=None):
        # nodos: lista de 6 posiciones, None si no está asignado
        self.nodos = nodos if nodos is not None else [None] * 6
        # disponibles: conjunto de números del 1 al 6 que aún no se han usado
        self.disponibles = disponibles if disponibles is not None else set(range(1, 7))

    def es_solucion(self):
        """Verifica si el estado es una solución válida."""
        if None in self.nodos:
            return False
        n1, n2, n3, n4, n5, n6 = self.nodos
        suma1 = n1 + n2 + n4  # Lado 1
        suma2 = n1 + n3 + n6  # Lado 2
        suma3 = n4 + n5 + n6  # Lado 3
        return suma1 == 10 and suma2 == 10 and suma3 == 10

    def generar_sucesores(self):
        """Genera los estados sucesores asignando un número disponible."""
        sucesores = []
        for i in range(len(self.nodos)):
            if self.nodos[i] is None:
                for num in self.disponibles:
                    nuevos_nodos = self.nodos.copy()
                    nuevos_nodos[i] = num
                    nuevos_disponibles = self.disponibles - {num}
                    sucesores.append(EstadoTriangulo(nuevos_nodos, nuevos_disponibles))
                break  # Solo asignamos al primer nodo vacío
        return sucesores

    def __str__(self):
        """Representación en cadena del triángulo."""
        if None in self.nodos:
            return "Estado incompleto"
        n1, n2, n3, n4, n5, n6 = self.nodos
        return f"  {n1}\n {n2} {n3}\n{n4} {n5} {n6}"

    def __eq__(self, other):
        """Compara dos estados para evitar duplicados."""
        if not isinstance(other, EstadoTriangulo):
            return False
        return self.nodos == other.nodos

    def __hash__(self):
        """Permite usar el estado en un conjunto (visitados)."""
        return hash(tuple(self.nodos))

class BuscadorTriangulo:
    def __init__(self):
        self.estado_inicial = EstadoTriangulo()

    def bfs(self):
        """Búsqueda en amplitud para encontrar una solución."""
        cola = deque([self.estado_inicial])
        visitados = set()

        while cola:
            estado = cola.popleft()
            if estado in visitados:
                continue
            visitados.add(estado)

            if estado.es_solucion():
                return estado

            sucesores = estado.generar_sucesores()
            cola.extend(sucesores)

        return None

    def dfs(self):
        """Búsqueda en profundidad para encontrar una solución."""
        pila = [self.estado_inicial]
        visitados = set()

        while pila:
            estado = pila.pop()
            if estado in visitados:
                continue
            visitados.add(estado)

            if estado.es_solucion():
                return estado

            sucesores = estado.generar_sucesores()
            pila.extend(sucesores)

        return None

# Prueba del programa
def main():
    buscador = BuscadorTriangulo()

    print("Buscando solución con BFS...")
    solucion_bfs = buscador.bfs()
    if solucion_bfs:
        print("Solución encontrada con BFS:")
        print(solucion_bfs)
    else:
        print("No se encontró solución con BFS.")

    print("\nBuscando solución con DFS...")
    solucion_dfs = buscador.dfs()
    if solucion_dfs:
        print("Solución encontrada con DFS:")
        print(solucion_dfs)
    else:
        print("No se encontró solución con DFS.")

if __name__ == "__main__":
    main()