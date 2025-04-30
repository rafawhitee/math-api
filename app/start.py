from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from app import create_app
from logger import logger
from config import Config
from exceptions.custom_exception import CustomException
from models.exception.custom_error import CustomError

app = create_app()

@app.get(f"{Config.PREFIX}/version")
def get_version():
    return { "version": Config.APP_VERSION }

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, error: Exception):
    logger.error(f"generic_exception_handler --> {error}", exc_info=True)
    return JSONResponse(status_code=500, content=CustomError(message=str(error)).to_dict())

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, error: HTTPException):
    logger.error(f"http_exception_handler --> {error}", exc_info=True)
    return JSONResponse(status_code=error.status_code, content=CustomError(message=error.detail).to_dict())

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, error: CustomException):
    logger.error(f"custom_exception_handler --> {error}", exc_info=True)
    return JSONResponse(status_code=error.code, content=CustomError(message=error.description).to_dict())