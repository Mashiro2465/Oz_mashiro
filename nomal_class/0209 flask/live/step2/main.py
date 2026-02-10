from flask import Flask
from flask_sock import Sock
import time
import threading

app = Flask(__name__)
sock = Sock(app)

conn = []

@sock.route("/ws")
def websocket(ws):
    conn.append(ws)
    while True:
        data = ws.receive() # postman에서 서버한테 주는 메시지

        if data is None:
            break

        ws.send(f"서버에서 보내는 메시지: {data}") # 서버가 postman에게 보내는 메시지
    conn.remove(ws)

def background_job():
    while True:
        time.sleep(5)
        for ws in list(conn):
            ws.send("5초마다 알림 발송 중")

threading.Thread(target=background_job, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)