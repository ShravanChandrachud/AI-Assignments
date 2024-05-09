from collections import defaultdict

class Graph:
    global x
    x = False
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited, search_vertex):
        visited[vertex] = True
        print(vertex, end=' ')
        if vertex == search_vertex:
            global x
            x = True

        for neighbor in self.graph[vertex]:
            if not x:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited, search_vertex)

    def dfs_wrapper(self, start_vertex, search_vertex):
        visited = [False] * (max(self.graph) + 1)
        print("Depth First Search (DFS): ")
        global x
        x =False
        self.dfs(start_vertex, visited, search_vertex)
        if x:
            print("Vertex found using DFS")
        else:
            print("Vertex not found using DFS")

    def bfs(self, start_vertex, search_vertex):
        visited = [False] * (max(self.graph) + 1)
        queue = [start_vertex]
        visited[start_vertex] = True

        print("Breadth First Search (BFS):")
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')
            if current_vertex == search_vertex:
                return True

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def CheckGraph(self):
        print(self.graph)


g = Graph()
print("Please input the undirected Graph:\n")

ch='Y'
node_ctr=0
while ch=='Y' or ch=='y':
    connected_nodes=int(input(f"Please enter number of connected nodes for node {node_ctr}: "))
    for i in range(0,connected_nodes):
        node_con=int(input(f"Enter connected node for node number {node_ctr}: "))
        g.add_edge(node_ctr,node_con)
    node_ctr+=1
    ch=input("Do you want to continue? Y/N : ")

start_vertex = int(input("Enter Starting index: "))
Ctrl = True
while Ctrl:
    choice = int(input("Enter your choice\n1. Depth First Search\n2. Breadth First Search\n3. Exit\n"))
    if choice == 1:
        search_vertex = int(input("Enter search vertex: "))
        g.dfs_wrapper(start_vertex, search_vertex)
        Ctrl = True
    elif choice==2:
        search_vertex = int(input("Enter search vertex: "))
        y = False
        y = g.bfs(start_vertex, search_vertex)
        if y:
            print("Vertex found using BFS")
        else:
            print("Vertex not found using BFS")
        Ctrl = True
    else:
        Ctrl = False