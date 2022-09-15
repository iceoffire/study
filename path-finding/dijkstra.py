import grp
from path import AdjacencyList

class Dijkstra:
    def __init__(self):
        pass

    def calculate(self, graph: AdjacencyList, point_a: int, point_b: int):
        open = [point_a] # yet to explore...
        map = { point_a: 0 } # expense to reach the specific point
        history = {}
        
        while len(open) > 0:
            current = min(open, key=lambda v: map[v])
            open.remove(current)
            cost = map[current]
            for neighbor in graph.vertices[current].edges:
                edge = graph.vertices[current].edges[neighbor]
                if (neighbor in open):
                    continue
                candidate = cost + edge.calculateFactor()
                if (neighbor in map and candidate > map[neighbor]):
                    continue
                if (neighbor in history):
                    continue
                map[neighbor] = candidate
                open.append(neighbor)
                history[neighbor] = current
        route = []
        current = point_b
        while current != point_a:
            route.append(current)
            current = history[current]
        route.append(current)
        route.reverse()
        return route