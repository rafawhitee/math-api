from typing import Any
from fastapi import HTTPException, status
from sympy import Eq, symbols, solve, sympify, simplify, factor
from sympy.core.sympify import SympifyError
from models.requests.equation_request import EquationRequest
from models.responses.equation_response import EquationResponse

class EquationService:
    
    def resolve(self, req: EquationRequest) -> EquationResponse:
        try:
            expression: str = req.expression
            target: str = req.target

            vars: Any = symbols(req.variables)    
            expression_sympy: Any = sympify(expression)
            expression_simplified: Any = simplify(expression)
            expression_factored: Any = factor(expression)

            target_sympy: Any = sympify(target)

            equation: Any = Eq(expression_sympy, target_sympy)
            solutions = solve(equation, vars)
            return EquationResponse(input=str(expression), simplified=str(expression_simplified), 
                                      factored=str(expression_factored),
                                      solutions=[str(s) for s in solutions])
        except SympifyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )