from exceptions.custom_exception import CustomException

class NotFoundException(CustomException):
    def __init__(self, description=None):
        super().__init__(code=404, description=description or 'Recurso não encontrado')