from typing import Any
from fastapi import HTTPException, status
from sympy import Eq, symbols, solve, sympify, simplify, factor
from sympy.core.sympify import SympifyError
from models.requests.expression_request import ExpressionRequest
from models.responses.expression_response import ExpressionResponse

class ExpressionService:
    
    def resolve_equation(self, req: ExpressionRequest) -> ExpressionResponse:
        """
        Resolve a function expression given as a string and return its roots.

        :param expr_str: String of the mathematical expression, e.g., 'x**2 - 4*x'
        :return: Dictionary with steps or error
        """
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
            return ExpressionResponse(input=str(expression), simplified=str(expression_simplified), 
                                      factored=str(expression_factored),
                                      solutions=[str(s) for s in solutions])
        except SympifyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )