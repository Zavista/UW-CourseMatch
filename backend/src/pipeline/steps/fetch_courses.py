from pipeline.pipe_step import PipeStep

class FetchCourses(PipeStep):
    
    def process(self, data):
        major = data["major"]
        term = data["term"]
        
        courses = [
            {"code": "CS135", "name": "Designing Functional Programs"},
            {"code": "CS136", "name": "Elementary Algorithm Design and Data Abstraction"},
            {"code": "CS246", "name": "Object-Oriented Software Development"},
            {"code": "CS241", "name": "Foundations of Sequential Programs"},
            {"code": "CS345", "name": "Introduction to Databases"},
            {"code": "CS444", "name": "Operating Systems"},
            {"code": "CS488", "name": "Artificial Intelligence"}
        ]

        return {**data, "courses": courses}