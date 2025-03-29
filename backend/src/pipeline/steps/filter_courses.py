from pipeline.pipe_step import PipeStep
import logging

logger = logging.getLogger(__name__)

class FilterCourses(PipeStep):
    def process(self, data):
        logger.info("Starting FilterCourses step.")
        
        taken_courses = set(data["past_courses"])

        # Directly filter the courses list
        data["courses"] = [
            course for course in data["courses"]
            if course["courseCode"] not in taken_courses and course["associatedAcademicCareer"] == data["academic_level"]
        ]
        
        logger.info(f"FilterCourses step completed. {len(data['courses'])} courses remain after filtering.")
        
        return data
