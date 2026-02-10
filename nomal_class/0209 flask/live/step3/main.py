from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def index():
    return render_template("typing.html")

@sock.route("/ws")
def websocket(ws):
    while True:
        data = ws.receive() # postman에서 서버한테 주는 메시지

        if data == "typing":
            ws.send("입력중...")
            
        elif data == "stop":
            ws.send("")

        if data is None:
            break

        ws.send(f"서버에서 보내는 메시지: {data}") # 서버가 postman에게 보내는 메시지

if __name__ == "__main__":
    app.run(debug=True)