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
