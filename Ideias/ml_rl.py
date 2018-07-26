import numpy as np
import pylab as plt

import networkx as nx

points_list = [(0,1), (3,2), (5,7), (2, 1), (2,7)]

goal = 5

G = nx.Graph()
G.add_edges_from(points_list)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()