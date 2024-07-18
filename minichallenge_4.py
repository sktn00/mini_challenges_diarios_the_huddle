# Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.
# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
from collections import deque
from typing import Dict, List


def bfs(graph: Dict[int, List[int]], start: int) -> None:
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(f"Visited node: {node}")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Representacion del graph
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3: [1], 4: [1, 2]}

# Iniciar BFS desde el nodo 0
print("Recorrido BFS:")
bfs(graph, 0)
