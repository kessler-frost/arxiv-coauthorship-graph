from sys import path
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections
from data_loader import get_arxiv_couthor_connect_edges


def create_graph():

    G = nx.Graph()
    edges = get_arxiv_couthor_connect_edges()
    for u, v in edges:
        if len(G.nodes) < 500:
            G.add_edge(u, v, weight=1)
        else:
            break

    return G


def pickle_graph():
    nx.write_gpickle(create_graph(), "graph.pkl")


def get_graph_from_pickle():
    return nx.read_gpickle("graph.pkl")


def grapher():
    # Get graph from pickle
    G = get_graph_from_pickle()

    # Draw the graph
    plt.figure()
    plt.title("Graph")
    nx.draw_networkx(G)

    # To plot Degree Distribution Histogram
    degree_seq = np.sort([d for _, d in G.degree()])[::-1]
    degree_count = collections.Counter(degree_seq)
    deg, cnt = zip(*degree_count.items())

    plt.figure()
    plt.bar(deg, cnt)

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")

    # Closeness centrality Histogram
    closeness_seq = nx.closeness_centrality(G)
    vertex, closeness = zip(*closeness_seq.items())

    plt.figure()
    plt.bar(vertex, closeness)

    plt.title("Closeness Histogram")
    plt.xlabel("Vertices")
    plt.ylabel("Closeness")

    # Betweenness centrality Histogram
    betweenness_seq = nx.betweenness_centrality(G)
    vertex, betweenness = zip(*betweenness_seq.items())

    plt.figure()
    plt.bar(vertex, betweenness)

    plt.title("Betweenness Histogram")
    plt.xlabel("Vertices")
    plt.ylabel("Betweenness")

    plt.show()


grapher()
