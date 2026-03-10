import networkx as nx

def astar_path(graph,start,end):

    G = nx.Graph()

    for node,edges in graph.items():
        for neighbour,weight in edges:
            G.add_edge(node,neighbour,weight=weight)

    path = nx.astar_path(G,start,end)

    return path
