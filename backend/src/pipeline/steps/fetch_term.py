from pipeline.pipe_step import PipeStep
from services.uw_api_client import UWAPIClient

class FetchTerm(PipeStep):
    def __init__(self):
        self.api_service = UWAPIClient()

    def process(self, data):
        print('1')
        term_data = self.api_service.fetch_term()
        print("2")

        return {**data, "termCode": term_data.get("termCode", "")}