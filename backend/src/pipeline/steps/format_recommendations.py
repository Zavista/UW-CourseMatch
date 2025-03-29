from pipeline.pipe_step import PipeStep

import logging
logger = logging.getLogger(__name__)

class FormatRecommendations(PipeStep):
    def process(self, data):
        logger.info("Starting FormatRecommendations step.")

        for recommendation in data["recommendations"]:
            course = next((course for course in data["courses"] if course["courseCode"] == recommendation["courseCode"]), None)
            
            if course:
                recommendation["description"] = course.get("description", "No description available")
                
        logger.info("FormatRecommendations step completed successfully.")
        return data