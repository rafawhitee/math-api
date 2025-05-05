from typing import Any
from fastapi import HTTPException, status
from sympy import simplify, factor
from sympy.core.sympify import SympifyError
from models.requests.expression_request import ExpressionRequest
from models.responses.expression_response import ExpressionResponse

class ExpressionService:
    
    def simplify(self, req: ExpressionRequest) -> ExpressionResponse:
        try:
            expression: str = req.expression
            expression_simplified: Any = simplify(expression)
            expression_factored: Any = factor(expression)
            return ExpressionResponse(input=str(expression), simplified=str(expression_simplified), 
                                      factored=str(expression_factored))
        except SympifyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )