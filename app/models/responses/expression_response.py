from typing import Optional
from pydantic import BaseModel

class ExpressionResponse(BaseModel):
    input: str
    simplified: Optional[str] = None
    factored: Optional[str] = None