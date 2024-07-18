# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
from typing import Dict, List


def dfs(graph: Dict[int, List[int]], start: int, visited: set = None) -> None:
    if visited is None:
        visited = set()

    visited.add(start)
    print(f"Visited node: {start}")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Representacion del graph
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2]}

# Iniciar DFS desde el nodo 0
print("Recorrido DFS:")
dfs(graph, 0)
