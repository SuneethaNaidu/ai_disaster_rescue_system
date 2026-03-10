from routing.graph_data import graph
from routing.dijkstra import dijkstra_path
from routing.astar import astar_path

def run_evacuation():

    start="A"
    safe="E"

    route = dijkstra_path(graph,start,safe)

    return route
