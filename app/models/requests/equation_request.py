from typing import List, Optional
from pydantic import BaseModel, Field

class EquationRequest(BaseModel):
    expression: str
    simplify: Optional[bool] = True
    factor: Optional[bool] = True
    variables: Optional[List[str]] = Field(default_factory=lambda: ["x"])
    target: Optional[str] = "0"