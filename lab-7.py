'''
import networkx as nx

G = nx.path_graph(4)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])

G = nx.cycle_graph(4)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])


G = nx.cycle_graph(4)
G.add_edge(0, 2)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print("c(", n, ")=", centrality[n])
'''

'''
import networkx as nx

#---directed graph---
G = nx.DiGraph(directed=True)

# add nodes
G.add_node("Singapore")
G.add_node("San Francisco")
G.add_node("Tokyo")
G.add_nodes_from(["Riga", "Copenhagen"])

# add edges
G.add_edge("Singapore","San Francisco")
G.add_edge("San Francisco","Tokyo")
G.add_edges_from(
    [
        ("Riga","Copenhagen"),
        ("Copenhagen","Singapore"),
        ("Singapore","Tokyo"),
        ("Riga","San Francisco"),
        ("San Francisco","Singapore"),
    ]
)
# set layout
pos = nx.circular_layout(G)

# draw graph
nx.draw(G, pos, with_labels = True)

# draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("Singapore","Tokyo"): '2 flights daily', 
        ("San Francisco","Singapore"): '5 flights daily',
    },
    font_color='red'
)
'''
import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
