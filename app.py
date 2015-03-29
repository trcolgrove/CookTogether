from flask import *

app=Flask(__name__)
@app.route("/")

def index():
    return "hi"

@app.route("/hi")

def info():
    if "balls" in request.args:
        return request.args["balls"]
    else:
        return "no balls found"

@app.route("/<arg>")

def args(arg=None):
    return arg
if __name__ == "__main__":
    app.run(debug=True)
