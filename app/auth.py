# /app/auth.py
from passlib.context import CryptContext
from typing import List, Dict


import requests


JWK = Dict[str, str]
JWKS = Dict[str, List[JWK]]

COGNITO_REGION = "us-west-1"
COGNITO_POOL_ID=COGNITO_REGION+"_fCWtjFI4Y"
def get_jwks() -> JWKS:
    return requests.get(
        f"https://cognito-idp.{COGNITO_REGION}'.amazonaws.com/"
        f"{COGNITO_POOL_ID}/.well-known/jwks.json"
    ).json()

get_jwks()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)
