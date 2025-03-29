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
    logging.info("Root endpoint accessed.")
    return {"message": "Welcome to the UW CourseMatch API!"}


@app.post("/match")
def match_courses(user_input: UserInput):
    logging.info("MatchCourses endpoint accessed.")
    pipeline = Pipeline()

    pipeline.add_step(Step.FETCH_TERM)
    pipeline.add_step(Step.FETCH_COURSES)
    pipeline.add_step(Step.FILTER_COURSES)
    pipeline.add_step(Step.FORMAT_PROMPT)
    pipeline.add_step(Step.RECOMMEND_COURSES)

    response = pipeline.run(user_input.model_dump())
    logging.info("MatchCourses endpoint completed successfully.")
    return response.get("recommendations", [])


from services.uw_api_client import UWAPIClient
@app.get("/test/{termCode}/{subject}")
def test(termCode: str, subject: str):
    logging.info(f"Test endpoint accessed with termCode={termCode} and subject={subject}.")
    client = UWAPIClient()
    courses = client.fetch_courses(termCode, subject)
    if not courses:
        logging.info("No courses found in Test endpoint.")
        return {"message": "No courses found"}
    logging.info("Test endpoint completed successfully.")
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)