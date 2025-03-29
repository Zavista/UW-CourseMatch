from pipeline.pipe_step import PipeStep
import logging

logger = logging.getLogger(__name__)

class RecommendCourses(PipeStep):

    def process(self, data):
        logger.info("Starting RecommendCourses step.")
        recommendations = [
            {"code": "CS345", "name": "Introduction to Databases"},
            {"code": "CS444", "name": "Operating Systems"},
            {"code": "CS488", "name": "Artificial Intelligence"}
        ]
        logger.info(f"RecommendCourses step completed. {len(recommendations)} recommendations generated.")
        return {**data, "recommendations": recommendations}