class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def min_key(self, key, mst_set):
        min_val = float("inf")
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and mst_set[v] == False:
                min_val = key[v]
                min_index = v

        return min_index

    def minimal_spanning_tree(self):
        parent = [-1] * self.V
        key = [float("inf")] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def print_mst(self, parent):
        total_weight = 0
        print("Edge \tWeight")
        for i in range(1, self.V):
            if parent[i] != -1:
                print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
                total_weight += self.graph[i][parent[i]]
        print("Total Weight:", total_weight)

def create_graph():
    V = int(input("Enter the number of vertices: "))
    g = Graph(V)
    while True:
        u = int(input("Enter the starting vertex of the edge (or -1 to finish): "))
        if u == -1:
            break
        v = int(input("Enter the ending vertex of the edge: "))
        weight = int(input("Enter the weight of the edge: "))
        g.add_edge(u, v, weight)
    return g

g = create_graph()
parent = g.minimal_spanning_tree()
g.print_mst(parent)
