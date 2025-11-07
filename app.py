from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", titulo = "derrollo web con flask y jinj2")

if __name__ == "__main__":
    app.run(debug = True)