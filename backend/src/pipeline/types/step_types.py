from enum import Enum

from pipeline.steps.fetch_courses import FetchCourses
from pipeline.steps.filter_courses import FilterCourses
from pipeline.steps.format_prompt import FormatPrompt
from pipeline.steps.recommend_courses import RecommendCourses

class Step(Enum):
    FETCH_COURSES = FetchCourses
    FILTER_COURSES = FilterCourses
    FORMAT_PROMPT = FormatPrompt
    RECOMMEND_COURSES = RecommendCourses