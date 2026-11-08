
import heapq


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v, weight, directed=False):
        if weight < 0:
            raise ValueError("Алгоритм Дейкстри не працює з від'ємними вагами")
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))
        if not directed:
            self.adj[v].append((u, weight))


def dijkstra(graph: Graph, start):
    """Повертає (distances, previous) — найкоротші відстані та попередників."""
    distances = {v: float("inf") for v in graph.adj}
    previous = {v: None for v in graph.adj}
    distances[start] = 0

    heap = [(0, start)]
    visited = set()

    while heap:
        dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph.adj[u]:
            new_dist = dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                previous[v] = u
                heapq.heappush(heap, (new_dist, v))

    return distances, previous


def build_path(previous, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous[target]
    return path[::-1]


if __name__ == "__main__":
    g = Graph()
    edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("B", "D", 10),
        ("C", "E", 3), ("E", "D", 4), ("D", "F", 11), ("E", "F", 7),
        ("F", "G", 1), ("E", "G", 9),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    start = "A"
    distances, previous = dijkstra(g, start)

    print(f"Найкоротші шляхи від вершини {start}:")
    print(f"{'Вершина':<8}{'Відстань':<10}Шлях")
    for v in sorted(distances):
        d = distances[v]
        path = " -> ".join(build_path(previous, v)) if d != float("inf") else "—"
        print(f"{v:<8}{d!s:<10}{path}")
