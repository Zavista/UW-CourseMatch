from pipeline.pipe_step import PipeStep
import logging
import re

logger = logging.getLogger(__name__)

class FormatPrompt(PipeStep):

    def process(self, data):
        logger.info("Starting FormatPrompt step.")

        def extract_prereqs(requirements_desc):
            """Extracts the prerequisite part of the requirementsDescription."""
            if not requirements_desc:  # Check if requirements_desc is None or empty
                return "None"  # Return a default value if no prerequisites are found

            # Proceed with regex only if requirements_desc is a valid string
            match = re.search(r"Prereq: (.*?);", requirements_desc)
            if match:
                return match.group(1).strip()  # Return the part between "Prereq:" and the first semicolon
            return "None"  # Default value if no prerequisites are found

        # Processing courses to extract prerequisites and format course information
        courses_info = [
            {
                "courseCode": course["courseCode"],
                "title": course["title"],
                "requirementsDescription": extract_prereqs(course.get("requirementsDescription", "")),
                "description": course["descriptionAbbreviated"],
            }
            for course in data['courses']
        ]

        # Formatting the prompt with explicit JSON instruction
        formatted_prompt = (
            f"You are an AI course advisor. The student is majoring in {data['subject']} and has completed the following courses: {', '.join(data['past_courses'])}. "
            f"For the upcoming term ({data['termCode']}), they have the following courses to choose from: "
            + ", ".join([f"{course['courseCode']}: {course['title']} (Description: {course['description']}, Prerequisites: {course['requirementsDescription']})" for course in courses_info]) +
            " Please recommend 3 courses for this student that will best align with their academic background and future career goals. "
            "Make sure to consider the following factors when making your recommendations: "
            "- The prerequisites of each course and how they fit with the student's previous courses "
            "- How the course will help the student develop foundational skills in their field "
            "- The relevance of the course to the student's major and future academic or career goals "
            "Respond strictly in **JSON format**. The response must contain a list of exactly 3 course recommendations in the following structure: "
            "1. Each item in the list should be a valid JSON object with the following keys and values: "
            "- 'courseCode' (string): The course code (e.g., 'CS101') "
            "- 'title' (string): The course title (e.g., 'Introduction to Programming') "
            "- 'description' (string): The course description "
            "2. Ensure there are no extra explanations or text outside of the JSON output. "
            "3. The JSON must be valid, well-formed, and include the correct punctuation, indentation, and structure. "
            "4. Do not include any extra lines, comments, or non-JSON text. "
            "Here’s an example output with placeholder data: "
            "{"
            "\"recommendations\":"
            "["
            "{"
            "\"courseCode\": \"<courseCode1>\","
            "\"title\": \"<courseTitle1>\","
            "\"description\": \"<courseDescription1>\"}, "
            "{ "
            "\"courseCode\": \"<courseCode2>\","
            "\"title\": \"<courseTitle2>\","
            "\"description\": \"<courseDescription2>\"}, "
            "{ "
            "\"courseCode\": \"<courseCode3>\","
            "\"title\": \"<courseTitle3>\","
            "\"description\": \"<courseDescription3>\"} ] }"
            "Ensure there are no extra lines, explanations, or text outside the JSON. "
            "The output must exactly match the provided format without any deviation."
        )

        logger.info("FormatPrompt step completed. Prompt formatted successfully.")

        return {**data, "prompt": formatted_prompt}
