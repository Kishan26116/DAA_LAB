# Kruskal's Algorithm

# Find the parent of a vertex
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


# Join two sets
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


# Kruskal's Algorithm
def kruskal(vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])

    parent = {}
    rank = {}

    # Initialize parent and rank
    for vertex in vertices:
        parent[vertex] = vertex
        rank[vertex] = 0

    mst = []
    total_cost = 0

    # Select edges one by one
    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # Add edge if it does not form a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, u, v)

    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(u, "-", v, ":", weight)

    print("Total Cost:", total_cost)


# Vertices
vertices = ['A', 'B', 'C', 'D', 'E']

# Edges: (source, destination, weight)
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5),
    ('C', 'E', 6),
    ('D', 'E', 7)
]

# Call Kruskal's Algorithm
kruskal(vertices, edges)