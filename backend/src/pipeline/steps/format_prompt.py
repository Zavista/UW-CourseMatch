from pipeline.pipe_step import PipeStep
import logging

logger = logging.getLogger(__name__)

class FormatPrompt(PipeStep):

    def process(self, data):
        logger.info("Starting FormatPrompt step.")
        formatted_prompt = (
            f"You are an AI course advisor helping a student choose their next courses. "
            f"The student is majoring in {data['subject']} and has previously taken: {', '.join(data['past_courses'])}. "
            f"For the upcoming term ({data['termCode']}), they can choose from the following courses:\n\n"
            + "\n".join(
                [f"- {course['courseCode']}: {course['title']} - {course['description']}" for course in data['courses']]
            ) +
            "\n\n"
            "Recommend 3 courses that would best complement the student's academic background and interests. "
            "Consider factors like prerequisite knowledge, skill progression, and relevance to their major. "
            "Respond in JSON format as a list of dictionaries, where each dictionary contains:\n"
            "  - 'codeCourse': The course code (e.g., 'CS642')\n"
            "  - 'title': The course title (e.g., 'Principles of Programming Languages')\n"
            "  - 'description': A brief description of the course\n\n"
            "Example output:\n"
            "[\n"
            "  {\"codeCourse\": \"<courseCode1>\", \"title\": \"<courseTitle1>\", \"description\": \"<courseDescription1>\"},\n"
            "  {\"codeCourse\": \"<courseCode2>\", \"title\": \"<courseTitle2>\", \"description\": \"<courseDescription2>\"},\n"
            "  {\"codeCourse\": \"<courseCode3>\", \"title\": \"<courseTitle3>\", \"description\": \"<courseDescription3>\"}\n"
            "]"
        )
        logger.info("FormatPrompt step completed. Prompt formatted successfully.")
        return {**data, "prompt": formatted_prompt}