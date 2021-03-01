from fastapi import FastAPI, WebSocket, Request, Depends
from static.html_templates.homepage import homepage
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from static.main import image_DIR
from schedulers import scheduler
from config import settings
from sockets import manager
from dependencies import *
from main import api
import time

@api.get("/")
def welcome():
    return HTMLResponse(homepage.format(docs_url=settings.API_BASE_URL+'/docs', company_url=settings.COMPANY_URL))

@api.on_event('startup')
async def startup_event():
    scheduler.start()

@api.on_event('shutdown')
async def shutdown_event():
    scheduler.shutdown()

@api.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@api.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

from routers.user_router import main as user

api.include_router(user.router, prefix="/admin", tags=["admin"], dependencies=[Depends(validate_bearer)])
