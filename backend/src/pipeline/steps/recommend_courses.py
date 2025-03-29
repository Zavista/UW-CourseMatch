from pipeline.pipe_step import PipeStep
from services.cohere_client import CohereClient
import json
import logging

logger = logging.getLogger(__name__)

class RecommendCourses(PipeStep):
    def __init__(self):
        self.cohere_client = CohereClient()

    def process(self, data):
        logger.info("Starting RecommendCourses step.")
        prompt = data["prompt"]
        
        recommendations_json = self.cohere_client.get_recommendations(prompt)

        if recommendations_json:
            try:
                # Parse the raw string to a dictionary
                recommendations_dict = json.loads(recommendations_json)

                # Check if the response is in the expected JSON format
                if "recommendations" in recommendations_dict:
                    # If the response is valid, update the data
                    data["recommendations"] = recommendations_dict["recommendations"]
                    logger.info("RecommendCourses step completed successfully.")
                else:
                    data["recommendations"] = {"error": "Recommendations key missing in response"}

            except json.JSONDecodeError as e:
                logger.error(f"JSONDecodeError: {str(e)}")
                data["recommendations"] = {"error": "Invalid JSON response from Cohere"}
            except Exception as e:
                logger.error(f"Error processing response: {str(e)}")
                data["recommendations"] = {"error": f"Error processing response: {str(e)}"}

        else:
            data["recommendations"] = {"error": "Failed to fetch recommendations"}

        return data
