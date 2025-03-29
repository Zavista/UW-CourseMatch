from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)

load_dotenv()


@app.post("/api/v1/match")
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)