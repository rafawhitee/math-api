from fastapi import HTTPException, Request, status


def get_bearer_token(request: Request) -> str:  
    if request == None or not isinstance(request, Request):
        raise HTTPException(status_code=400, detail="No request found")
            
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    parts = auth_header.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return parts[1]