import networkx as nx
from collections import deque
import matplotlib.pyplot as plt
import graph as gh



if __name__ == "__main__":
    
    #1 buat graf
    edges=[(1, 2), (1, 3), (2, 3), (3, 4), (4, 7)]
    G=gh.create_graph(edges)

    #2 hitung derajat
    node = 3
    a = gh.get_degree(G, node)
    print("derajatnya:", a)

    #dfs
    start = 1
    b = gh.dfs_traversal(G, start)
    print(f"DFS Traversal dri vertex{start}: {b}")

    #bfs
    start = 2
    c = gh.bfs_traversal(G, start)
    print(f"BFS Traversal dri vertex {start}: {c}")

    source= 7
    target= 3
    d=gh.find_shortest_path(G, source, target)
    print(d)
    gh.visualize_graph(G)

