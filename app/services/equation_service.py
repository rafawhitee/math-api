import sympy as sp
from typing import Any
from fastapi import HTTPException, status
from models.requests.equation_request import EquationRequest
from models.responses.equation_response import EquationResponse

class EquationService:
    
    def resolve(self, req: EquationRequest) -> EquationResponse:
        try:
            vars: Any = sp.symbols(req.variables)    
            expression_sympy: Any = sp.sympify(req.expression)
            target_sympy: Any = sp.sympify(req.target)

            if req.simplify:
                expression_simplified: Any = str(sp.simplify(expression_sympy))
            else:
                expression_simplified = None

            if req.factor:
                expression_factored: Any = str(sp.factor(expression_sympy))
            else:
                expression_factored = None

            equation: Any = sp.Eq(expression_sympy, target_sympy)
            solutions = sp.solve(equation, vars)
            return EquationResponse(input=str(req.expression), simplified=expression_simplified, 
                                      factored=expression_factored,
                                      solutions=[str(s) for s in solutions])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )