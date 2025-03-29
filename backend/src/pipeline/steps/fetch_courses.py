from pipeline.pipe_step import PipeStep
from services.uw_api_client import UWAPIClient


class FetchCourses(PipeStep):
    def __init__(self):
        self.api_service = UWAPIClient()

    def process(self, data):
        subject = data["subject"]
        termCode = data.get("termCode")

        print('3')
        raw_courses = self.api_service.fetch_courses(termCode, subject)
        print("4")
        formatted_courses = []

        for course in raw_courses:
            course_data = {
                "courseCode": f"{course["subjectCode"]}{course["catalogNumber"]}",
                "title": course["title"],
                "description": course["description"],
            }

            formatted_courses.append(course_data)
        

        return {**data, "courses": formatted_courses}