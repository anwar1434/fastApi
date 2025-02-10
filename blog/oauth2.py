from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token  # ✅ This is the correct import

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(access_token: str = Depends(oauth2_scheme)):  # ✅ Rename token -> access_token
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token.verify_token(access_token, credentials_exception)  # ✅ Now this calls the correct module