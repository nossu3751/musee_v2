import os

import requests
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from passlib.context import CryptContext

from .JWTBearer import JWKS, JWTBearer, JWTAuthorizationCredentials

load_dotenv()  # Automatically load environment variables from a '.env' file.

# jwks = JWKS.parse_obj(
#     requests.get(
#         f"https://cognito-idp.{os.environ.get('COGNITO_REGION')}.amazonaws.com/"
#         f"{os.environ.get('COGNITO_POOL_ID')}/.well-known/jwks.json"
#     ).json()
# )

# auth = JWTBearer(jwks)


# async def get_current_user(
#     credentials: JWTAuthorizationCredentials = Depends(auth)
# ) -> str:
#     try:
#         return credentials.claims["username"]
#     except KeyError:
        # HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Username missing")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)