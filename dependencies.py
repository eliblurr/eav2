from fastapi import Header, HTTPException, Depends 
from main import oauth2_scheme

async def validate_bearer(token:str=Depends(oauth2_scheme)):
    # validate token
    # validate role
    return 'sd'
