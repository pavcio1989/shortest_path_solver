import sys
import logging
# Add content root to your path
sys.path.append('C:/Users/pawel/Desktop/Learning/shortest_path_solver')

if __name__ == "__main__":
    from src.config.config import Config
    from src.loggers.sp_logger import SPLogger
    from src.pipelines.pipeline import Pipeline

    logger = SPLogger(__name__, level=logging.INFO)

    config = Config()

    pipeline = Pipeline(config)

    pipeline.run()
