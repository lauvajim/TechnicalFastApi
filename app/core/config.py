from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime, timezone, timedelta


SECRET_KEY = "clave_secreta"
TOKEN_EXPIRE_MINUTES: int = 30
ALGORITHM = "HS256"

def create_access_token(data:dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (timedelta(minutes=TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)