from flask import Flask, redirect, url_for, render_template, request
from writing_prompts import generate_prompts

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate1", methods=["POST", "GET"])
def generate1():
    return redirect(url_for("output", amt = 1))

@app.route("/generate5", methods=["POST", "GET"])
def generate5():
    return redirect(url_for("output", amt = 5))

@app.route("/<amt>")
def output(amt):
    return render_template("index.html", results = generate_prompts(int(amt)))

if __name__ == "__main__":
    app.run(debug=True)

