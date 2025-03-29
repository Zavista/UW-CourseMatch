from pipeline.pipe_step import PipeStep
import logging

logger = logging.getLogger(__name__)

class FilterCourses(PipeStep):

    def process(self, data):
        logger.info("Starting FilterCourses step.")
        taken_courses = set(data["past_courses"])

        filtered_courses = [
            course for course in data["courses"] if course["courseCode"] not in taken_courses
        ]
        logger.info(f"FilterCourses step completed. {len(filtered_courses)} courses remain after filtering.")
        return {**data, "filtered_courses": filtered_courses}