from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.manager import manager

router = APIRouter(prefix="/websoket", tags=["Websoket"])

@router.websocket("/ws/notifications")
async def notification_socket(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:

        manager.disconnect(websocket)