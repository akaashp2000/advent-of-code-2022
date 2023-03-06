class MapGraph:
    def __init__(self, vertices, edges, inverted=False):
        self.vertices = vertices
        self.edges = edges

        if inverted:
            self.edges = {}

    def shortest_distance(self, start, end):
        visited = [start]

        layers = {0: [start]}
        layer = 0
        while end not in visited:

            layers[layer+1] = []

            for vertex in layers[layer]:
                for neighbour in [edge[1] for edge in self.edges[vertex]]:
                    if neighbour not in visited:
                        layers[layer + 1].append(neighbour)
                        visited.append(neighbour)

            layer += 1

        return layer

    def shortest_distance_multiple(self, start, ends):
        visited = [start]
        
        layers = {0: [start]}
        layer = 0
        while True:
            layers[layer+1] = []

            for vertex in layers[layer]:
                for neighbour in [edge[1] for edge in self.edges[vertex]]:
                    if neighbour not in visited:
                        layers[layer + 1].append(neighbour)
                        visited.append(neighbour)
                        if neighbour in ends:
                            return layer + 1
            layer += 1