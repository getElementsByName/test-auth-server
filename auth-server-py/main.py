from fastapi import FastAPI, Request
import socket
from routes import jwt_router

app = FastAPI(debug=True)


@app.get("/")
def read_root():
    return "AUTH SERVER"

@app.get("/healthcheck")
def healthcheck():
    return "OK"

@app.get("/info")
def info(request: Request):
    # https://www.starlette.io/requests/
    info = {
        "client.host": request.client.host,
        "url": request.url,
        "header": request.headers,
        "cookies": request.cookies,
        "hostname": socket.gethostname()
    }
    return info


app.include_router(jwt_router.router)