from flask import Flask, render_template, request
from detector import check_url

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        message = request.form["url"]

        result = check_url(message)

        history.insert(0, {
            "message": message,
            "result": result
        })

    return render_template(
        "index.html",
        result=result,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)