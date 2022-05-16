from fastapi import APIRouter, Request, Response
import env
from routes.jwt_util import decode_jwt
import re
import jwt

router = APIRouter()


jwt_hmac_secret = env.ENV_JWT_HMAC_SECRET
AUTH_HEADER_NAME = "Authorization"
VALUE_TYPE = "Bearer"
RESPONSE_HEADER_PREFIX = 'AUTH-'

@router.get("/auth/jwt")
def auth_jwt(request: Request, response: Response, field_list: str = None):
    auth_raw_value = request.headers.get(AUTH_HEADER_NAME)
    jwt_encorded_value = re.sub(rf"^{VALUE_TYPE}\W*", '', auth_raw_value)
    try:
        jwt_json = decode_jwt(jwt_encorded_value, secret=jwt_hmac_secret)
    except jwt.exceptions.InvalidSignatureError:
        response.status_code = 500
        return 'InvalidSignatureError'
    
    field_list_str = field_list
    if field_list_str:
        field_list = field_list_str.split(',')
        for field_str in field_list:
            field_normalized_str = field_str.capitalize()
            field_value = jwt_json.get(field_str)
            response.headers[f"{RESPONSE_HEADER_PREFIX}{field_normalized_str}"] = field_value
    
    return jwt_json
    
    
  