from fastapi import APIRouter
from config import Config
from services.expression_service import ExpressionService
from models.requests.expression_request import ExpressionRequest
from models.responses.expression_response import ExpressionResponse

service = ExpressionService()

expressions_router = APIRouter(
    prefix=f"{Config.PREFIX}/v1/expressions",
    tags=["functions"]
)

@expressions_router.get("", response_model=ExpressionResponse)
@expressions_router.get("/", response_model=ExpressionResponse)
def resolve_equation(expression_request: ExpressionRequest):
   return service.resolve_equation(expression_request)