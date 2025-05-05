from fastapi import APIRouter
from config import Config
from services.function_service import FunctionService
from models.requests.function_request import FunctionRequest
from models.responses.function_response import FunctionResponse

service = FunctionService()

functions_router = APIRouter(
    prefix=f"{Config.PREFIX}/v1/math/functions",
    tags=["functions"]
)

@functions_router.post("", response_model=FunctionResponse)
@functions_router.post("/", response_model=FunctionResponse)
def resolve(req: FunctionRequest):
   return service.evaluate(req)