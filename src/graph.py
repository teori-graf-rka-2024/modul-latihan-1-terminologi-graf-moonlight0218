import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Membuat graf
def create_graph(edges: list[tuple[int, int]]):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)]
G = create_graph(edges)

# Menghitung derajat simpul
def get_degree(G: nx.Graph, node: int):
    return G.degree(node)



# DFS Traversal
def dfs_traversal(G: nx.Graph, start: int):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:  
            visited.add(node)
            traversal.append(node)
            stack.extend(sorted(G.neighbors(node), reverse=True))

    return traversal



# BFS Traversal (Perbaikan nx.Grapdh → nx.Graph)
def bfs_traversal(G: nx.Graph, start: int):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(sorted(G.neighbors(node)))

    return traversal


# 
def find_shortest_path(G: nx.Graph, source: int, target: int):
    if not G.has_node(source) or not G.has_node(target):
        return []
    
    queue = deque([[source]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == target:
            return path
        
        if node not in visited:
            visited.add(node)

            for neighbor in G.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)

    return []
    source=5
    target=3
    d=find_shortest_path(G, source, target)
    print(d)

def visualize_graph(G: nx.Graph):
    plt.figure(figsize=(5, 5))  # Ukuran plot
    pos = nx.spring_layout(G)  # Posisi node otomatis
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    plt.show()
