from typing import List, Optional
from pydantic import BaseModel

class FunctionSolutionResponse(BaseModel):
    variable: str
    value: str

class FunctionResponse(BaseModel):
    input: str
    solutions: Optional[List[FunctionSolutionResponse]] = []