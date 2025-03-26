from pipeline.pipe_step import PipeStep

class FilterCourses(PipeStep):

    def process(self, data):
        taken_courses = set(data["past_courses"])
        filtered_courses = [
            course for course in data["courses"] if course["code"] not in taken_courses
        ]
        return {**data, "filtered_courses": filtered_courses}