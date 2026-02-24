from fastapi import WebSocket, FastAPI, WebSocketDisconnect
import random

app = FastAPI()


@app.websocket("/ws/game")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    random_number = random.randint(1, 100)
    attemps = 0
    await websocket.send_text("게임시작합니다 1~100사이 숫자를 입력하세요")

    try:
        while True:
            data = await websocket.receive_text()
            guess_number = int(data)

            attemps += 1

            if guess_number == random_number:
                await websocket.send_text(f"정답입니다{attemps}회 입력하셨습니다")
                break
            elif guess_number > random_number:
                await websocket.send_text(f"down {attemps}회 입력하셨습니다")
            elif guess_number < random_number:
                await websocket.send_text(f"up {attemps}회 입력하셨습니다")

    except WebSocketDisconnect:
        await websocket.close()
