import cohere
import logging
import os

logger = logging.getLogger(__name__)

class CohereClient:
    """
    A client to interact with the Cohere API for generating course recommendations.
    """

    def __init__(self):
        """
        Initializes the CohereClient with the API key from environment variables.
        """
        self.api_key = os.getenv("COHERE_API_KEY")
        if not self.api_key:
            raise ValueError("COHERE_API_KEY is not set in environment variables")
        self.client = cohere.ClientV2(self.api_key)

    def get_recommendations(self, prompt: str):
        """
        Sends a formatted prompt to the Cohere API and retrieves course recommendations.

        Args:
            prompt (str): The formatted prompt to send to the Cohere API.

        Returns:
            str: A JSON string containing course recommendations, or None if an error occurs.
        """
        logger.info("Sending prompt to Cohere API for recommendations.")
        try:
            response = self.client.chat(
                model="command-a-03-2025",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
            )
            recommendations_text = response.message.content[0].text.lstrip("|START_RESPONSE|>")
            logger.info(f"Received response from Cohere API: {recommendations_text[:100]}...")  # Log first 100 chars
            return recommendations_text
        except Exception as e:
            logger.error(f"Error while calling Cohere API: {e}")
            return None
