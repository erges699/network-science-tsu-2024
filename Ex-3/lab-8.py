''' Случайный граф. Генерация графа Эрдёша-Реньи

import networkx as nx

G = nx.erdos_renyi_graph(0, 1.0)
for n in G.nodes():
    print(G.degree(n))
'''

'''Вычисление средней степени вершин графа

import networkx as nx

G = nx.erdos_renyi_graph(10, 0.2)
a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(float(a) / len(G.nodes()))
'''
