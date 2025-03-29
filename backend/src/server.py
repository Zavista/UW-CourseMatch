from fastapi import FastAPI
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Logs to console
    ],
)

from models.user_input import UserInput
from pipeline.pipeline import Pipeline
from pipeline.types.step_types import Step

app = FastAPI(
    version="0.1.0",
    title="UW CourseMatch API",
    description="A simple API to match students with courses"
)

load_dotenv()

@app.get("/")
def read_root():
    """
    Root endpoint to verify the API is running.
    """
    logging.info("Root endpoint accessed.")
    return {"message": "Welcome to the UW CourseMatch API!"}


@app.post("/match")
def match_courses(user_input: UserInput):
    """
    Matches courses for a student based on their input.

    Args:
        user_input (UserInput): The student's input including subject, academic level, and past courses.

    Returns:
        list: A list of recommended courses.
    """
    logging.info("MatchCourses endpoint accessed.")
    pipeline = Pipeline()

    pipeline.add_step(Step.FETCH_TERM)
    pipeline.add_step(Step.FETCH_COURSES)
    pipeline.add_step(Step.FILTER_COURSES)
    pipeline.add_step(Step.FORMAT_PROMPT)
    pipeline.add_step(Step.RECOMMEND_COURSES)
    pipeline.add_step(Step.FORMAT_RECOMMENDATIONS)

    response = pipeline.run(user_input.model_dump())
    logging.info("MatchCourses endpoint completed successfully.")
    return response.get("recommendations", [])


from services.uw_api_client import UWAPIClient
@app.get("/test/{termCode}/{subject}")
def test(termCode: str, subject: str):
    """
    Test endpoint to fetch courses for a given term and subject.

    Args:
        termCode (str): The term code.
        subject (str): The subject code.

    Returns:
        dict: A dictionary containing the fetched courses or an error message.
    """
    logging.info(f"Test endpoint accessed with termCode={termCode} and subject={subject}.")
    client = UWAPIClient()
    courses = client.fetch_courses(termCode, subject)
    if not courses:
        logging.info("No courses found in Test endpoint.")
        return {"message": "No courses found"}
    logging.info(f"Test endpoint completed successfully. Found {len(courses)} courses.")
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)