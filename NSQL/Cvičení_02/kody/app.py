from flask import Flask, render_template, request, redirect, url_for, flash
from redis import Redis
import os

SECRET_KEY = os.urandom(32)
USER_IMG_FOLDER = 'static/imgs/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = USER_IMG_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY


user_reviews = {
    "pepa": {
        "review": "Hele fakt bomba website, ale chybi mi tu vlastne vsechno",
        "img": os.path.join(app.config['UPLOAD_FOLDER'], "man.png")
    },
    "franta": {
        "review": "Chtel jsem najit recept na smazeny vajicka, ale dostal jsem se tu. Nevi jak.",
        "img": os.path.join(app.config['UPLOAD_FOLDER'], "dog.png")
    },
    "alena": {
        "review": "Produkt teto firmy je nejlepsi. Pouzivame ho vsichni. Obcas ho pujcime i dedeckovi.",
        "img": os.path.join(app.config['UPLOAD_FOLDER'], "woman.png")
    }
}

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    counter = 1
    #TODO: cesta se musí pak změnit v Docker řešení :)
    news = ["news/" + filename for filename in os.listdir("./code/templates/news")]
    print(news)
    return render_template("index.html", reviews=user_reviews, view_count=counter, news_list=news)

@app.route("/review/<username>")
def get_review(username):
    if username in user_reviews:
        return f"Returning requested review. {username}:{user_reviews[username]}"
    else:
        return "Username not found in database."

@app.route("/datasets")
def datasets():
    return render_template("datasets.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        if 'image' not in request.files:
            flash('Image not uploaded!')
        elif request.files['image'] == "":
            flash('Image not uploaded!')
        else:
            file = request.files['image']
            basedir = os.path.abspath(os.path.dirname(__file__))
            relative_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            absolute_path = os.path.join(basedir, relative_path)
            file.save(absolute_path)
            user_name = request.form.get("username")
            user_review = request.form.get("review")
            user_reviews[user_name] = {"review": user_review, "img": relative_path}
            flash('Review was successfully saved!')
        return redirect(url_for("contact"))
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)