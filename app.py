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


# Login Function
@app.route("/")
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        '''check if username exists in db '''
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            '''ensure hashed password matches user input'''
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                '''invalid password match'''
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            '''username doesn't exist'''
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


# Register Function
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        ''' check if username already exists in db'''
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

        '''put the new user into 'session' cookie'''
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("add_manager"))
    return render_template("signup.html")


# Logout Function
@app.route("/logout")
def logout():
    '''remove user from session cookie'''
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


# Displays Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''grab the session user's username from db'''
    managers = mongo.db.managers.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, managers=managers)

    return redirect(url_for("log_in"))


# Add New Manager details on Login
@app.route("/add_manager", methods=["GET", "POST"])
def add_manager():
    '''allows the user to add manager details'''
    if request.method == "POST":
        manager = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "team_name": request.form.get("team_name"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "created_by": session["user"]
        }
        mongo.db.managers.insert_one(manager)
        flash("Manager Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))
    manager = mongo.db.managers.find()
    return render_template("add_manager.html", manager=manager)


# Edits Manager Details
@app.route("/edit_manager/<manager_id>", methods=["GET", "POST"])
def edit_manager(manager_id):
    '''allows the user to update and edit manager details'''
    if request.method == "POST":
        submit = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "team_name": request.form.get("team_name"),
            "email": request.form.get("email"),
            "contact_number": request.form.get("contact_number"),
            "created_by": session["user"]
        }
        mongo.db.managers.update({"_id": ObjectId(manager_id)}, submit)
        flash("Manager Successfully Updated")
        return redirect(url_for('profile', username=session['user']))
    manager = mongo.db.managers.find_one({"_id": ObjectId(manager_id)})
    managers = mongo.db.managers.find()
    return render_template(
        "edit_manager.html", manager=manager, managers=managers)


# Displays Squad
@app.route("/get_squad")
def get_squad():
    '''displays all players in the squad'''
    squad = mongo.db.squad.find().sort("last_name", 1)
    return render_template("squad.html", squad=squad)


# Search Squad Function
@app.route("/search_player", methods=["GET", "POST"])
def search_player():
    '''alows the user to search the squad for a specific player or players'''
    search = request.form.get("search")
    squad = mongo.db.squad.find({"$text": {"$search": search}})
    return render_template("squad.html", squad=squad)


# Add player Function
@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    '''alows the user to add a new player to the users squad'''
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


# Update Player Function
@app.route("/udpate_player/<player_id>", methods=["GET", "POST"])
def update_player(player_id):
    '''alows the user to edit a players details'''
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
            "injured": injured,
            "created_by": session["user"]
        }
        mongo.db.squad.update({"_id": ObjectId(player_id)}, submit)
        flash("Player Successfully Updated")
        return redirect(url_for("get_squad"))
    player = mongo.db.squad.find_one({"_id": ObjectId(player_id)})
    squad = mongo.db.squad.find()
    return render_template("edit_player.html", player=player, squad=squad)


# Delete Player Function
@app.route("/delete_player/<player_id>")
def delete_player(player_id):
    '''allows the user to delete a player'''
    mongo.db.squad.remove({"_id": ObjectId(player_id)})
    flash("Player Successfully Deleted")
    return redirect(url_for("get_squad"))


# Displays Fixtures and Results
@app.route("/get_fixtures")
def get_fixtures():
    '''displays all fixtures and results'''
    fixtures = mongo.db.fixtures.find().sort("date", 1)
    results = mongo.db.fixtures.find().sort("date", 1)
    return render_template("fixtures.html", fixtures=fixtures, results=results)


# Add Fixture Function
@app.route("/add_fixture", methods=["GET", "POST"])
def add_fixture():
    '''alows the user to create a new fixture'''
    if request.method == "POST":
        fixture = {
            "home_team": request.form.get("home_team"),
            "away_team": request.form.get("away_team"),
            "date": request.form.get("date"),
            "kick_off": request.form.get("kick_off"),
            "home_goals": "null",
            "away_goals": "null",
            "created_by": session["user"]
        }
        mongo.db.fixtures.insert_one(fixture)
        flash("Fixture Successfully Added")
        return redirect(url_for("get_fixtures"))
    fixture = mongo.db.fixtures.find()
    return render_template("add_fixture.html", fixture=fixture)


# Update Fixture Function
@app.route("/udpate_fixture/<fixture_id>", methods=["GET", "POST"])
def update_fixture(fixture_id):
    if request.method == "POST":
        '''alows the user to update a fixture'''
        submit = {
            "home_team": request.form.get("home_team"),
            "away_team": request.form.get("away_team"),
            "date": request.form.get("date"),
            "kick_off": request.form.get("kick_off"),
            "home_goals": request.form.get("home_goals"),
            "away_goals": request.form.get("away_goals"),
            "created_by": session["user"]
        }
        mongo.db.fixtures.update({"_id": ObjectId(fixture_id)}, submit)
        flash("Fixture Successfully Updated")
        return redirect(url_for("get_fixtures"))
    fixture = mongo.db.fixtures.find_one({"_id": ObjectId(fixture_id)})
    fixtures = mongo.db.fixtures.find()
    return render_template(
        "edit_fixture.html", fixture=fixture, fixtures=fixtures)


# Delete Fixture Function
@app.route("/delete_fixture/<fixture_id>")
def delete_fixture(fixture_id):
    '''alows the user to delete a fixture'''
    mongo.db.fixtures.remove({"_id": ObjectId(fixture_id)})
    flash("Fixture Successfully Deleted")
    return redirect(url_for("get_fixtures"))


# Update Result Function
@app.route("/udpate_result/<result_id>", methods=["GET", "POST"])
def update_result(result_id):
    if request.method == "POST":
        '''alows the user to update a result'''
        submit = {
            "home_team": request.form.get("home_team"),
            "away_team": request.form.get("away_team"),
            "date": request.form.get("date"),
            "kick_off": request.form.get("kick_off"),
            "home_goals": request.form.get("home_goals"),
            "away_goals": request.form.get("away_goals"),
            "created_by": session["user"]
        }
        mongo.db.fixtures.update({"_id": ObjectId(result_id)}, submit)
        flash("Result Successfully Updated")
        return redirect(url_for("get_fixtures"))
    result = mongo.db.fixtures.find_one({"_id": ObjectId(result_id)})
    results = mongo.db.fixtures.find()
    return render_template(
        "edit_result.html", result=result, results=results)


# Delete Result Function
@app.route("/delete_result/<result_id>")
def delete_result(result_id):
    '''alows the user to delete a result'''
    mongo.db.fixtures.remove({"_id": ObjectId(result_id)})
    flash("Result Successfully Deleted")
    return redirect(url_for("get_fixtures"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
