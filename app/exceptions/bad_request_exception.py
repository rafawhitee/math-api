from exceptions.custom_exception import CustomException

class BadRequestException(CustomException):
    def __init__(self, description=None):
        super().__init__(code=400, description=description or 'Requisição inválida')