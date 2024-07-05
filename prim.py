import heapq

def prim(graph, start_node):
    mst = set([start_node])
    edges = [
        (cost, start_node, to)
        for to ,cost in graph[start_node].items()
        if to != start_node
    ]
    heapq.heapify(edges)

    total_cost = 0

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in mst:
            mst.add(to)
            total_cost += cost 
            print(f"Edge: {frm} -> {to}, Cost: {cost}")
            for to_next, cost2 in graph[to].items():
                if to_next not in mst and to != start_node:
                    heapq.heappush(edges, (cost2, to, to_next))

    print(f"\nOverall MST Cost: {total_cost}")

num_nodes = int(input("Enter the number of nodes: "))
graph = {}
for i in range(num_nodes):
    node = input(f"Enter node {i+1} name: ")
    graph[node] = {}
    num_neighbours = int(input(f"Enter the number of neighbours for node {node}: "))
    for j in range(num_neighbours):
        neighbour = input(f"Enter neighbour {j+1} name for node {node}: ")
        cost = int(input(f"Enter the cost of edge between node {node} and neighbour {neighbour}: "))
        graph[node][neighbour] = cost

start_node = input("Enter the start node: ")

print("\nMinimum Spanning Tree edges:")
prim(graph, start_node)