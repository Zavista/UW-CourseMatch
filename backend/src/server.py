from fastapi import FastAPI


from models.user_input import UserInput
from pipeline.pipeline import Pipeline

from pipeline.steps.fetch_courses import FetchCourses
from pipeline.steps.filter_courses import FilterCourses
from pipeline.steps.format_prompt import FormatPrompt
from backend.src.pipeline.steps.recommend_courses import RecommendCourses

app = FastAPI(
    version="0.1.0",
    title="UW CourseMatch API",
    description="A simple API to match students with courses"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the UW CourseMatch API!"}


@app.post("/match")
def match_courses(user_input: UserInput):

    pipeline = Pipeline()

    pipeline.add_step(FetchCourses())
    pipeline.add_step(FilterCourses())
    pipeline.add_step(RecommendCourses())
    pipeline.add_step(FormatPrompt())

    response = pipeline.run(user_input.model_dump())

    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True)