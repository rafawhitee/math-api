from fastapi import APIRouter
from config import Config
from services.equation_service import EquationService
from models.requests.equation_request import EquationRequest
from models.responses.equation_response import EquationResponse

service = EquationService()

equations_router = APIRouter(
    prefix=f"{Config.PREFIX}/v1/math/equations",
    tags=["equations"]
)

@equations_router.post("", response_model=EquationResponse)
@equations_router.post("/", response_model=EquationResponse)
def resolve(req: EquationRequest):
   return service.resolve(req)