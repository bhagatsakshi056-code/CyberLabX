from database import init_db
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Stores deployed labs temporarily
running_labs = []


@app.route("/")
def home():
    return render_template("index.html", labs=running_labs)


@app.route("/deploy/<lab_name>")
def deploy_lab(lab_name):

    if lab_name not in running_labs:
        running_labs.append(lab_name)

    return redirect(url_for("home"))


@app.route("/delete/<lab_name>")
def delete_lab(lab_name):

    if lab_name in running_labs:
        running_labs.remove(lab_name)

    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)