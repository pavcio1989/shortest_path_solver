from abc import abstractmethod
from collections import defaultdict
import networkx as nx

from src.config.config import Config
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge


class ShortestPathBaseSolver:
    def __init__(self, config: Config):
        self.n = config.node_count
        self.s = config.source_id
        self.t = config.sink_id
        self.graph = defaultdict(list)
        self.config = config

        self.visited = self.n * [False]

    @abstractmethod
    def solve(self):
        pass

    def add_directed_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

    def add_undirected_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])
            self.add_edge(edge_raw[1], edge_raw[0], edge_raw[2])

    def add_edge(self, start_node, end_node, cost):
        edge1 = Edge(start_node, end_node, cost)

        self.graph[start_node].append(edge1)

    def get_directed_graph(self):
        self.solve()

        # Create empty NX directed graph
        dg = nx.Graph()

        # TODO: Fill graph with nodes and edges

        return dg
