from pipeline.pipe_step import PipeStep

class FormatPrompt(PipeStep):
    
    def process(self, data):
        formatted_prompt = (
            f"User is in {data['major']} and has taken {', '.join(data['past_courses'])}. "
            f"Suggest 3 additional courses from this list: {', '.join([c['code'] for c in data['filtered_courses']])}."
        )

        return {**data, "prompt": formatted_prompt}