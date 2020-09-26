import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections

# Peterson Graph
G = nx.petersen_graph()

# Random Graph
# G = nx.gnp_random_graph(100, 0.02)

# Draw the graph
plt.figure()
plt.title("Graph")
nx.draw(G, with_labels=True, font_weight='bold')

# To plot Degree Distribution Histogram
degree_seq = np.sort([d for _, d in G.degree()])[::-1]
degree_count = collections.Counter(degree_seq)
deg, cnt = zip(*degree_count.items())

plt.figure()
plt.bar(deg, cnt)

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")


# Diameter of the Graph
diameter = nx.algorithms.distance_measures.diameter(G)
print("Diameter of the graph is: ", diameter)

# Closeness centrality(inwards) Histogram
closeness_seq = nx.algorithms.centrality.closeness_centrality(G)
vertex, closeness = zip(*closeness_seq.items())

plt.figure()
plt.bar(vertex, closeness)

plt.title("Closeness Histogram")
plt.xlabel("Vertices")
plt.ylabel("Closeness")

plt.show()
