from typing import List, Optional
from pydantic import BaseModel

class ExpressionResponse(BaseModel):
    input: str
    simplified: Optional[str] = None
    solutions: Optional[List[str]] = []