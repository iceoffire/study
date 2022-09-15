from typing import Tuple

class Vertice: # vertice
    def __init__(self, coord: Tuple, city: str):
        self.x = coord[0]
        self.y = coord[1]
        self.city = city
        self.edges = {}
    
    def add_edges(self, edges):
        self.edges = edges

class Connection:
    def __init__(self, distance: float): # save properties to use later in the algorithm
        self.distance = distance
    
    def calculateFactor(self):
        return self.distance

class AdjacencyList:
    def __init__(self):
        self.vertices = []
    
    def add_vertex(self, vertice):
        self.vertices.append(vertice)
        return self.vertices.index(vertice)
    
    def connect(self, i_a, i_b): # adjacency list
        distance = self.__calculate_distance(self.vertices[i_a], self.vertices[i_b])
        self.vertices[i_a].edges[i_b] = Connection(distance)
        self.vertices[i_b].edges[i_a] = Connection(distance)

    def __calculate_distance(self, coord_a, coord_b):
        delta_x = coord_b.x - coord_a.x
        delta_y = coord_b.y - coord_a.y
        return (delta_x**2 + delta_y**2)**0.5 # hypotenuse
