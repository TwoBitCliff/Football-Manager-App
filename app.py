import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_profile")
def get_profile():
    squad = mongo.db.squad.find()
    return render_template("base.html", squad=squad)


@app.route("/")
@app.route("/get_squad")
def get_squad():
    squad = mongo.db.squad.find()
    return render_template("squad.html", squad=squad)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "first_name": request.form.get("first_name").capitalize(),
            "last_name": request.form.get("last_name").capitalize(),
            "contact_number": request.form.get("contact_number"),
            "team_name": request.form.get("team_name").capitalize()
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful!")

        session["user"] = request.form.get("first_name")
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
