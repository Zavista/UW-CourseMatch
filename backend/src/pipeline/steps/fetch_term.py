from pipeline.pipe_step import PipeStep

class FetchTerm(PipeStep):
    
    def process(self, data):
        return {**data, "term": "1201"}