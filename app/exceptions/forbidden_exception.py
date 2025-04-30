from exceptions.custom_exception import CustomException

class ForbiddenException(CustomException):
    def __init__(self, description=None):
        super().__init__(code=403, description=description or 'Acesso negado')