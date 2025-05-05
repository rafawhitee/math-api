import sympy as sp
from fastapi import HTTPException, status
from models.requests.expression_request import ExpressionRequest
from models.responses.expression_response import ExpressionResponse

class ExpressionService:
    
    def simplify(self, req: ExpressionRequest) -> ExpressionResponse:
        try:
            return ExpressionResponse(input=str(req.expression), simplified=str(sp.simplify(req.expression)), 
                                      factored=str(sp.factor(req.expression)))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )