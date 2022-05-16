from fastapi import APIRouter, Request, Response

router = APIRouter()





@router.get("/ratelimit")
def ratelimit(request: Request, response: Response):
  
  return ""
  