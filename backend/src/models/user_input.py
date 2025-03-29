from pydantic import BaseModel
from typing import List

class UserInput(BaseModel):
    subject: str
    past_courses: List[str]