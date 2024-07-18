# Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que
# encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.
from collections import deque
from typing import Dict, List, Union


def shortest_path(
    graph: Dict[int, List[int]], start: int, end: int
) -> Union[List[int], None]:
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


graph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

start_node = 0
end_node = 4
path = shortest_path(graph, start_node, end_node)

if path:
    print(
        f"Shortest path from {start_node} to {end_node}: {' -> '.join(map(str, path))}"
    )
    print(f"Path length: {len(path) - 1}")
else:
    print(f"No path found from {start_node} to {end_node}")
