from pipeline.pipe_step import PipeStep
from services.uw_api_client import UWAPIClient
import logging

logger = logging.getLogger(__name__)

class FetchTerm(PipeStep):
    def __init__(self):
        self.api_service = UWAPIClient()

    def process(self, data):
        logger.info("Starting FetchTerm step.")
        term_data = self.api_service.fetch_term()
        logger.info(f"FetchTerm step completed. Term code: {term_data.get('termCode', '')}")
        return {**data, "termCode": term_data.get("termCode", "")}