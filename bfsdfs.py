class Graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)
        
    def DFS(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)
    
    def BFS(self, s):
        visited = set()
        queue = [s]
        visited.add(s)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

g = Graph()
num_edges = int(input("Enter the number of edges: "))
print("Now enter the edges (u, v): ")
for i in range(num_edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)

print("DFS, Enter the starting vertex: ")
start_vertex = int(input())
g.DFS(start_vertex, set())

print("\nBFS, Enter the starting vertex: ")
start_vertex = int(input())
g.BFS(start_vertex)