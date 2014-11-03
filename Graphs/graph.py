class DirectedGraph():
    def __init__(self):
        self.g = {}

    def add_edge(self, nodeA, nodeB):
        self.g[nodeA] = nodeB

    def getNeighboursFor(self, node):
        result = []
        for key in self.g:
            if self.g[key] == node:
                result.append(key)
        return str(result)

    def to_string(self):
        return str(self.g)

    def path_between(self, nodeA, nodeB):
        current = nodeA
        visited = []
        while True:
            for key in self.g:
                if current == nodeB:
                    return True
                else:
                    if key == current:
                        current = self.g[key]
                    elif current in visited:
                        return False
                    else:
                        visited.append(current)

