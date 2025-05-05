from fastapi import APIRouter
from config import Config
from services.expression_service import ExpressionService
from models.requests.expression_request import ExpressionRequest
from models.responses.expression_response import ExpressionResponse

service = ExpressionService()

expressions_router = APIRouter(
    prefix=f"{Config.PREFIX}/v1/math/expressions",
    tags=["expressions"]
)

@expressions_router.get("", response_model=ExpressionResponse)
@expressions_router.get("/", response_model=ExpressionResponse)
def simplify(req: ExpressionRequest):
   return service.simplify(req)