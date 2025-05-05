def format_solution(sol):
    if isinstance(sol, dict):
        return {str(k): str(v) for k, v in sol.items()}
    return str(sol)