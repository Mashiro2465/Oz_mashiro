from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def home() :
    return "Hello this is Main Page"

@app.route('/hello')
def hello() :
    return render_template("hello.html", name = "민석")

@app.route('/user/<username>')
def user(username) :
    return render_template("user.html", username = username)

@app.route('/fruits')
def fruits() :
    fruits = ["사과", "복숭아", "포도", "딸기", "수박"]
    return render_template("fruits.html", fruits = fruits)

@app.route('/input')
def input() :
    return render_template("input.html")
    
@app.route('/greet')
def greet():
    name = request.args.get("name")
    return render_template("greet.html", name=name)
    



if __name__ == "__main__" :
    print("__name__:", __name__)
    app.run()