from fastapi import HTTPException, status
from sympy import Eq, symbols, solve, sympify, simplify
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
            x = symbols('x')
            expression: str = req.expression
            expression_sympy = sympify(expression)
            simplified = simplify(expression_sympy)
            solutions = solve(Eq(simplified, 0), x)
            return ExpressionResponse(input=str(expression), simplified=str(simplified), solutions=[str(s) for s in solutions])
        except SympifyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )