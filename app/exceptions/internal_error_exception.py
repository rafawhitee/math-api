from exceptions.custom_exception import CustomException

class ServerInternalErrorException(CustomException):
    def __init__(self, description=None):
        super().__init__(code=500, description=description or 'Ocorreu um erro inesperado')