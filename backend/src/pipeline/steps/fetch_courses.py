from pipeline.pipe_step import PipeStep
from services.uw_api_client import UWAPIClient
import logging

logger = logging.getLogger(__name__)

class FetchCourses(PipeStep):
    def __init__(self):
        self.api_service = UWAPIClient()

    def process(self, data):
        subject = data["subject"]
        termCode = data.get("termCode")
        logger.info(f"Starting FetchCourses step for term {termCode} and subject {subject}.")
        raw_courses = self.api_service.fetch_courses(termCode, subject)
        formatted_courses = []

        for course in raw_courses:
            course_data = {
                "courseCode": f"{course['subjectCode']}{course['catalogNumber']}",
                "title": course["title"],
                "description": course["description"],
            }

            formatted_courses.append(course_data)

        logger.info(f"FetchCourses step completed. Retrieved {len(formatted_courses)} courses.")
        return {**data, "courses": formatted_courses}