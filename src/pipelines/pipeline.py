import logging
from collections import defaultdict

from src import solvers
from src.config.config import Config
from src.pipelines.names import SPSolver
from src.utils.visuals import visualize_minimum_spanning_tree


logger = logging.getLogger('sp')


class Pipeline:
    def __init__(self, config: Config):
        self.solvers = config.solvers
        self._output_image_folder_path = f"{config.output_image_folder}/{config.input_file_path.split('/')[-1].split('.')[-2]}"
        self.config = config

    def run(self):
        for solver_name in self.solvers:
            if self.solvers[solver_name]:
                logger.info(f"----****----")
                logger.info(f"Shortest path solver: {solver_name} | In scope: YES")

                # Initialize MaxFlow solver class
                solver: solvers.ShortestPathBaseSolver = \
                    getattr(solvers, SPSolver[solver_name].value)(self.config)

                # Create graph
                solver.add_undirected_edges()

                # TODO: Placeholder for solve() method call

                # TODO: Adjust image storing
                # dg, pos = solver.get_directed_graph()
                # _output_image_file_path = self._output_image_folder_path+"_flow_chart_"+solver_name+".png"
                # visualize_minimum_spanning_tree(dg, pos, _output_image_file_path, solver.get_mst().values())

            else:
                logger.info(f"Shortest path solver: {solver_name} | In scope: NO")
