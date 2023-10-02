from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)