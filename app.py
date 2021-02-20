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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    first_name = mongo.db.users.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, first_name=first_name)

    return redirect(url_for("log_in"))


@app.route("/")
@app.route("/get_squad")
def get_squad():
    squad = mongo.db.squad.find()
    return render_template("squad.html", squad=squad)


@app.route("/")
@app.route("/get_fixtures")
def get_fixtures():
    fixtures = mongo.db.fixtures.find()
    result = mongo.db.result.find()
    return render_template("fixtures.html", fixtures=fixtures, result=result)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("signup.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        injured = "on" if request.form.get("injured") else "off"
        player = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "age": request.form.get("age"),
            "position": request.form.get("position"),
            "foot": request.form.get("foot"),
            "played": request.form.get("played"),
            "goals": request.form.get("goals"),
            "assists": request.form.get("assists"),
            "yellow": request.form.get("yellow"),
            "red": request.form.get("red"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "injured": injured,
            "created_by": session["user"]
        }
        mongo.db.squad.insert_one(player)
        flash("Player Successfully Added")
        return redirect(url_for("get_squad"))
    squad = mongo.db.squad.find()
    return render_template("squad.html", squad=squad)


@app.route("/udpate_player/<player_id>", methods=["GET", "POST"])
def update_player(player_id):
    if request.method == "POST":
        injured = "on" if request.form.get("injured") else "off"
        submit = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "age": request.form.get("age"),
            "position": request.form.get("position"),
            "foot": request.form.get("foot"),
            "played": request.form.get("played"),
            "goals": request.form.get("goals"),
            "assists": request.form.get("assists"),
            "yellow": request.form.get("yellow"),
            "red": request.form.get("red"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "injured": injured
        }
        mongo.db.squad.update({"_id": ObjectId(player_id)}, submit)
        flash("Player Successfully Updated")
        return redirect(url_for("get_squad"))
    player = mongo.db.squad.find_one({"_id": ObjectId(player_id)})
    squad = mongo.db.squad.find()
    return render_template("edit_player.html", player=player, squad=squad)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
