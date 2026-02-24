from fastapi import WebSocket, FastAPI, WebSocketDisconnect
import psutil
import asyncio

app = FastAPI()


@app.websocket("/ws/monitor")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = {
                "cpu" : psutil.cpu_percent(),
                "ram" : psutil.virtual_memory().percent,
            }
            await websocket.send_json(data)
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        await websocket.close()
