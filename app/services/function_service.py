import sympy as sp
from typing import Any, List
from fastapi import HTTPException, status
from models.requests.function_request import FunctionRequest
from models.responses.function_response import FunctionResponse, FunctionSolutionResponse

class FunctionService:

    def evaluate(self, req: FunctionRequest) -> FunctionResponse:
        try:
            vars: Any = sp.symbols(req.variables)
            var_names: List[str] = [str(v) for v in vars]
            expression: Any = sp.sympify(req.expression)
            response: FunctionResponse = FunctionResponse(input=req.expression, solutions=[])

            if req.target:
                target_expr: Any = sp.sympify(req.target)
                equation: Any = sp.Eq(expression, target_expr)
            else:
                equation: Any = sp.Eq(expression, 0)

            provided_vars: set = set(req.values.keys())
            needed_vars: set = set(var_names)

            if needed_vars.issubset(provided_vars):
                ordered_values = [float(req.values[str(var)]) for var in vars]
                f = sp.lambdify(vars, expression)
                result = f(*ordered_values)
                response.solutions.append(FunctionSolutionResponse(variable=str(req.target), value=str(result)))
            else:
                unknown_vars: List[Any] = list(needed_vars - provided_vars)
                known_subs = {str(k): v for k, v in req.values.items()}

                subs_expr: Any = equation.subs(known_subs)
                solutions: Any = sp.solve(subs_expr, unknown_vars)

                if isinstance(solutions, dict):
                    sols = self.__create_solutions_responses_from_dict(solutions)
                    for sol in sols:
                        response.solutions.append(sol)

                elif isinstance(solutions, list):
                    for solution in solutions:
                        if isinstance(solution, dict):
                            dict_solutions = self.__create_solutions_responses_from_dict(solution)
                            for dict_solution in dict_solutions:
                                response.solutions.append(dict_solution)
                        else:
                            response.solutions.append(self.__create_solution_response(unknown_vars, solution))
                            
                else:
                    response.solutions.append(self.__create_solution_response(unknown_vars, solutions))

            return response
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )
        
    def __create_solutions_responses_from_dict(self, solutions: Any) -> List[FunctionSolutionResponse]:
        if not isinstance(solutions, dict):
            return None
        responses: List[FunctionSolutionResponse] = []
        for var, sol in solutions.items():
            responses.append(FunctionSolutionResponse(
                            variable=str(var),
                            value=str(sol)
                        ))
        return responses
    
    def __create_solution_response(self, unknown_vars: Any, solutions: Any) -> FunctionSolutionResponse:
        return FunctionSolutionResponse(
                            variable=unknown_vars[0] if unknown_vars else "?",
                            value=str(solutions)
                        )