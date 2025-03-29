import requests
import logging
import os

logger = logging.getLogger(__name__)

class UWAPIClient:
    """
    A client to interact with the University of Waterloo API.
    """

    def __init__(self):
        """
        Initializes the UWAPIClient with API URL and API key from environment variables.
        """
        self.api_url = os.getenv("UW_API_URL")
        self.api_key = os.getenv("UW_API_KEY")

    def fetch_courses(self, termCode: str, subject: str):
        """
        Fetches courses for a given term and subject from the UW API.

        Args:
            termCode (str): The term code for the desired term.
            subject (str): The subject code for the desired courses.

        Returns:
            list: A list of courses if the request is successful, otherwise an empty list.
        """
        API_URL = f"{self.api_url}/Courses/{termCode}/{subject}"
        headers = {"x-api-key": self.api_key}
        logger.info(f"Fetching courses for term '{termCode}' and subject '{subject}'.")
        try:
            response = requests.get(API_URL, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Successfully fetched {len(data)} courses for term '{termCode}' and subject '{subject}'.")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error while fetching courses: {response.status_code} - {response.text}")
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while fetching courses: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error while fetching courses: {e}")
            return []

    def fetch_term(self):
        """
        Fetches the current term from the UW API.

        Returns:
            dict: A dictionary containing the term information if the request is successful, otherwise an empty dictionary.
        """
        API_URL = f"{self.api_url}/Terms/current"
        headers = {"x-api-key": self.api_key}
        logger.info("Fetching the current term from the UW API.")
        try:
            response = requests.get(API_URL, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Successfully fetched the current term: {data.get('termCode', 'Unknown')}.")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error while fetching the current term: {response.status_code} - {response.text}")
            return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while fetching the current term: {e}")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error while fetching the current term: {e}")
            return {}
