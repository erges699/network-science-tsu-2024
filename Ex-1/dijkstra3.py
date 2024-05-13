import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_weighted_edges_from([
    ('s', 'u', 10), ('s', 'x', 5), ('u', 'v', 1), ('u', 'x', 2), 
    ('v', 'y', 1), ('x', 'u', 3), ('x', 'v', 5), ('x', 'y', 2), 
    ('y', 's', 7), ('y', 'v', 6)])
predecessors, _ = nx.floyd_warshall_predecessor_and_distance(G)
shortest_path_s_v = nx.reconstruct_path('s', 'v', predecessors)
edges = [(a,b) for a,b in zip(shortest_path_s_v, shortest_path_s_v[1:])]
weights = nx.get_edge_attributes(G, 'weight')
pos = nx.circular_layout(G)
nx.draw_networkx(G, pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
nx.draw_networkx_edges(G, pos=pos, edgelist=edges, edge_color="r", width=3)
title = "Shortest path between [{}] and [{}]: {}"\
        .format("s", "v", " -> ".join(shortest_path_s_v))
plt.title(title)
