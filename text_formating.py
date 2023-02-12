from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def run():
    return render_template("texts.html")


if __name__ == "__main__":
    app.run(debug=True)