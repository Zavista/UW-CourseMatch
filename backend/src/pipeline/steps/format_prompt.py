from pipeline.pipe_step import PipeStep

class FormatPrompt(PipeStep):
    
    def process(self, data):
        formatted_prompt = (
            f"User is in {data['subject']} and has taken {', '.join(data['past_courses'])}. "
            f"Suggest 3 additional courses from this list: {', '.join([c['courseCode'] for c in data['filtered_courses']])}. "
            "Please format the response as a JSON dictionary with 'code' and 'name' fields for each recommended course."
        )

        return {**data, "prompt": formatted_prompt}