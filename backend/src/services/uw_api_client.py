import requests
import logging
import os

class UWAPIClient:
    
    def __init__(self):
        self.api_url = os.getenv("UW_API_URL")
        self.api_key = os.getenv("UW_API_KEY")

    def fetch_courses(self, termCode: str, subject: str):
        print('5')
        API_URL = f"{self.api_url}/Courses/{termCode}/{subject}"
        headers = {
            "x-api-key": self.api_key
        }
        print(API_URL)
        try:
            response = requests.get(API_URL, headers=headers, timeout=5) 
            response.raise_for_status()  
            data = response.json()
            return data

        except requests.exceptions.HTTPError as e:
            logging.error(f"UW API request failed: {response.status_code} - {response.text}")
            return []
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error while calling UW API: {e}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return []
    
    def fetch_term(self):
        API_URL = f"{self.api_url}/Terms/current"
        headers = {
            "x-api-key": self.api_key
        }
        try:
            response = requests.get(API_URL, headers=headers, timeout=5) 
            response.raise_for_status()  
            data = response.json()
            return data
        except requests.exceptions.HTTPError as e:
            logging.error(f"UW API request failed: {response.status_code} - {response.text}")
            return {}
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error while calling UW API: {e}")
            return {}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {}
        