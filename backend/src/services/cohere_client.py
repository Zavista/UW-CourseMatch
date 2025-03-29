import cohere
import logging
import os

logger = logging.getLogger(__name__)

class CohereClient:
    def __init__(self):
        self.api_key = os.getenv("COHERE_API_KEY")  
        if not self.api_key:
            raise ValueError("COHERE_API_KEY is not set in environment variables")

        self.client = cohere.ClientV2(self.api_key)

    def get_recommendations(self, prompt: str):
        """Sends the formatted prompt to Cohere and retrieves course recommendations."""
        try:
            response = self.client.chat(
                model="command-a-03-2025",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format={"type": "json_object"},
            )

            # Parse the response text into a dictionary
            recommendations_text = response.message.content[0].text
            recommendations_text = recommendations_text.lstrip("|START_RESPONSE|>")
            logger.info(f"Raw response text from Cohere: {recommendations_text}")

            return recommendations_text  # Cohere should return a structured JSON string

        except Exception as e:
            logging.error(f"Error while calling Cohere API: {e}")
            return None
