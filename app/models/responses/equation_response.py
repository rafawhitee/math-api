from typing import List, Optional
from pydantic import BaseModel

class EquationResponse(BaseModel):
    input: str
    simplified: Optional[str] = None
    factored: Optional[str] = None
    solutions: Optional[List[str]] = []