from pipeline.pipe_step import PipeStep

class SelectCourses(PipeStep):

    def process(self, data):
        recommendations= [  
            {"code": "CS345", "name": "Introduction to Databases"},
            {"code": "CS444", "name": "Operating Systems"},
            {"code": "CS488", "name": "Artificial Intelligence"}
        ]
        return {**data, "recommendations": recommendations}