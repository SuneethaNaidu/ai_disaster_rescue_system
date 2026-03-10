import networkx as nx

def dijkstra_path(graph,start,end):

    G = nx.Graph()

    for node,edges in graph.items():
        for neighbour,weight in edges:
            G.add_edge(node,neighbour,weight=weight)

    path = nx.dijkstra_path(G,start,end)

    return path
