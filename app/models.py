from sqlmodel import SQLModel , Field

from typing import Optional
from datetime import datetime


class ResumeMatchResult(SQLModel , table=True):
    id:Optional[int] = Field(default=None , primary_key= True)
    filename : str
    match_score : str
    matched_keywords: str
    missing_keywords: str
    suggestions: str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    # created_at: datetime = Field(default_factory=datetime.utcnow)