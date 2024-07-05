class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        total_cost = 0  # Initialize total cost of MST
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                total_cost += w  # Add the weight of the edge to the total cost
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")
        print(f"Total cost of MST: {total_cost}")  # Print the total cost of MST

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        g.add_edge(u, v, w)
    g.kruskal_algo()

if __name__ == "__main__":
    main()
