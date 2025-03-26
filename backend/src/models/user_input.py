from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    major: str
    past_courses: List[str]