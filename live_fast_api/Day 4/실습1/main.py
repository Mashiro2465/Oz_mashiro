from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"서버 응답 : {data}")
    except WebSocketDisconnect:
        await websocket.close()
