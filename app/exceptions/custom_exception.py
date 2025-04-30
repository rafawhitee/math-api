from fastapi import HTTPException

class CustomException(HTTPException):
    def __init__(self, code:int = 500, description: str = None):
        self.code = code
        self.description = description or 'Ocorreu um erro inesperado'