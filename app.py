import wolframalpha
from flask import Flask, render_template, request
from helpers import graph, wolfram

# Configuring flask
app = Flask(__name__)
  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/derivative", methods=["GET", "POST"])
def derivative():
    if request.method == "POST":
        degree = request.form.get("deriv")
        method = " derivative of "
        expression = request.form.get("query")
        inp = degree + method + expression
        answer = wolfram(inp)

        return render_template("derivative.html", inp = inp, answer=answer)
    else:
        return render_template("derivative.html")


@app.route("/integral", methods=["GET", "POST"])
def integral():
    if request.method == "POST":
        method = "integrate"
        lower = request.form.get("lower")
        upper = request.form.get("upper")
        expression = request.form.get("function")
        inp = f"{method} {expression} from {lower} to {upper}"
        answer = wolfram(inp)
        print(inp)
        print(answer)

        return render_template("integral.html", inp=inp, answer=answer)
    else:
        return render_template("integral.html")

@app.route("/limit", methods=["GET", "POST"])
def limit():
    if request.method == "POST":
        # find the limit of function as it approaches c from left/right
        method = "lim "
        function = request.form.get("function")
        c = request.form.get("limitapproaches")
        side = request.form.get("side")

        additional = f" as x->{c}{side}"

        inp = method + function + additional
        answer = wolfram(inp)

        return render_template("limit.html", inp=inp, answer=answer)
    else:
        return render_template("limit.html")