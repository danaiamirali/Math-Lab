import wolframalpha
from flask import Flask, render_template, request
from helpers import graph, wolfram

# Configuring flask
app = Flask(__name__)
  

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        expression = request.form.get("query")
        answer = wolfram(expression)

        return render_template("calculated.html", input=expression, answer=answer)
    else:
        return render_template("calculate.html")


@app.route("/calculated", methods=["GET", "POST"])
def calculated():
    if request.method == "POST":
        return render_template("calculated.html")
    else:
        return render_template("/")

@app.route("/derivative", methods=["GET", "POST"])
def derivative():
    if request.method == "POST":
        method = "find the derivative of"
        expression = request.form.get("query")
        pass
    else:
        return render_template("derivative.html")


@app.route("/integral", methods=["GET", "POST"])
def integral():
    if request.method == "POST":
        method = "integrate"
    else:
        return render_template("integral.html")

@app.route("/limit", methods=["GET", "POST"])
def limit():
    if request.method == "POST":
        # find the limit of function as it approaches c from left/right
        podid = "Limit"
        method = "lim "
        function = request.form.get("function")
        c = request.form.get("limitapproaches")
        side = request.form.get("side")

        additional = f" as x->{c}{side}"

        inp = method + function + additional
        print(inp)
        answer = wolfram(inp, podid)

        return render_template("limit.html", inp=inp, answer=answer, post=True)
    else:
        return render_template("limit.html")