from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    major: str
    term: str
    past_courses: List[str]