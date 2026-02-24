from fastapi import WebSocket, FastAPI, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws/{nickname}")
async def websocket_endpoint(websocket: WebSocket, nickname: str):
    await websocket.accept()
    await websocket.send_text(f"{nickname}님 환영합니다 당신은 지금 서버와 1:1 연결되셨습니다")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"{nickname}: {data}")

    except WebSocketDisconnect:
        await websocket.close()
