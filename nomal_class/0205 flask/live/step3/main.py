from flask import Flask, render_template, jsonify

app = Flask(__name__)



@app.route('/user/<name>')
def user(name) :
    return jsonify(msg=f"{name}님, BE 캠프에 오신 걸 환영합니다")

if __name__ == "__main__":
    app.run(debug=True)