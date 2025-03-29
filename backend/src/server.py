from fastapi import FastAPI
from dotenv import load_dotenv

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
    return {"message": "Welcome to the UW CourseMatch API!"}


@app.post("/match")
def match_courses(user_input: UserInput):

    pipeline = Pipeline()

    pipeline.add_step(Step.FETCH_TERM)
    pipeline.add_step(Step.FETCH_COURSES)
    pipeline.add_step(Step.FILTER_COURSES)
    pipeline.add_step(Step.FORMAT_PROMPT)
    pipeline.add_step(Step.RECOMMEND_COURSES)

    response = pipeline.run(user_input.model_dump())

    return response


from services.uw_api_client import UWAPIClient
@app.get("/test/{termCode}/{subject}")
def test(termCode: str, subject: str):

    client = UWAPIClient()
    courses = client.fetch_courses(termCode, subject)
    if not courses:
        return {"message": "No courses found"}
    return courses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)