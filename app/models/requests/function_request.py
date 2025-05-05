from typing import Any, List, Optional
from pydantic import BaseModel, Field

class FunctionRequest(BaseModel):
    expression: str
    values: dict[str, float]
    target: Optional[str] = "y"
    variables: Optional[List[str]] = Field(default_factory=lambda: ["x", "y"])