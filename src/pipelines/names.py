from enum import Enum


class SPSolver(Enum):
    dijkstra = "DijkstraSPSolver"
    bellman_ford = "BellmanFordSPSolver"
    naive_heap = "NaiveHeapSPSolver"
