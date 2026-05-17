from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    name = request.form["name"]
    role = request.form["role"]
    confidence = request.form["confidence"]

    return render_template(
        "result.html",
        name=name,
        role=role,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
