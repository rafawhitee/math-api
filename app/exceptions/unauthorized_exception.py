from exceptions.custom_exception import CustomException

class UnauthorizedException(CustomException):
    def __init__(self, description=None):
        super().__init__(code=401, description=description or 'Acesso negado')