import requests
import logging
import os

logger = logging.getLogger(__name__)

class UWAPIClient:
    
    def __init__(self):
        self.api_url = os.getenv("UW_API_URL")
        self.api_key = os.getenv("UW_API_KEY")

    def fetch_courses(self, termCode: str, subject: str):
        API_URL = f"{self.api_url}/Courses/{termCode}/{subject}"
        headers = {
            "x-api-key": self.api_key
        }
        logger.info(f"Starting to fetch courses for term {termCode} and subject {subject}.")
        try:
            response = requests.get(API_URL, headers=headers, timeout=5) 
            response.raise_for_status()  
            data = response.json()
            logger.info(f"Successfully fetched courses for term {termCode} and subject {subject}.")
            return data

        except requests.exceptions.HTTPError as e:
            logger.error(f"UW API request failed: {response.status_code} - {response.text}")
            return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while calling UW API: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return []
    
    def fetch_term(self):
        API_URL = f"{self.api_url}/Terms/current"
        headers = {
            "x-api-key": self.api_key
        }
        logger.info("Starting to fetch the current term.")
        try:
            response = requests.get(API_URL, headers=headers, timeout=5) 
            response.raise_for_status()  
            data = response.json()
            logger.info("Successfully fetched the current term.")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"UW API request failed: {response.status_code} - {response.text}")
            return {}
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error while calling UW API: {e}")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {}
