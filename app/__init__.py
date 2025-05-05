import sys
import os
from fastapi import FastAPI

current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)

paths_to_add = [
    parent_dir,
    current_dir,
    os.path.join(current_dir, 'app'),
]

app_subdirs = [
    'routers',
    'config',
    'exceptions',
    'middlewares',
    'logger',
    'models',
    'services',
    'utils'
]

paths_to_add += [os.path.join(current_dir, 'app', subdir) for subdir in app_subdirs]

for path in paths_to_add:
    if path not in sys.path:
        sys.path.append(path)

def create_app():
    app = FastAPI(
        title="Math API",
        description="Serviços de Exatas",
        version="0.0.1",
        docs_url="/swagger-ui/",
        redoc_url="/redocs",
        openapi_url="/openapi.json"
    )

    from middlewares.custom_middleware import CustomMiddleware
    app.add_middleware(CustomMiddleware)

    from routers.math import expressions_router, equations_router
    app.include_router(equations_router.equations_router)
    app.include_router(expressions_router.expressions_router)
    return app