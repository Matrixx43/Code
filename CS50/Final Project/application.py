import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pingpong.db")


@app.route("/")
@login_required
def stats():
    # Get top 5 players user has played with
    # Get number of victories, losses and games played
    victories = 0
    losses = 0
    players = []
    information = db.execute("SELECT winner_id, loser_id FROM matches WHERE winner_id=:user_id OR loser_id=:user_id", user_id=session["user_id"])
    for dictionary in information:
        if dictionary["winner_id"] == session["user_id"]:
            victories += 1
            players.append(dictionary["loser_id"])
        else:
            losses += 1
            players.append(dictionary["winner_id"])
    # Transform their id into usernames
    usernames = []
    for item in players:
        username = db.execute("SELECT username FROM users WHERE id = :user_id", user_id=item)
        usernames.append(username[0]["username"])
    # Create a list to pass
    definitivelist = []
    # Create a list with all the usernames
    users_used = []
    for username in usernames:
        if username not in users_used:
            users_used.append(username)
    for user in users_used:
        # Count how many times it played
        count = 0
        for username in usernames:
            if username == user:
                count += 1
        # Add to definitivelist
        definitivelist.append([count, user])
    # Sort definitivelist by count and take only first five elements
    definitivelist = sorted(definitivelist, reverse=True)[:5]
    return render_template("stats.html", data=definitivelist, victories=victories, losses=losses, gamesplayed=victories + losses)


@app.route("/matches")
@login_required
def matches():
    table = db.execute("SELECT * FROM matches WHERE winner_id=:user_id OR loser_id=:user_id", user_id=session["user_id"])
    if not table:
        return apology("You havent played any matches yet")
    else:
        # Make a list with all the usernames in the dictionary
        winners = []
        losers = []
        for dictionary in table:
            winner = db.execute("SELECT username FROM users WHERE id =:user_id", user_id=dictionary["winner_id"])
            winners.append(winner[0]["username"])
            loser = db.execute("SELECT username FROM users WHERE id =:user_id", user_id=dictionary["loser_id"])
            losers.append(loser[0]["username"])
        return render_template("matches.html", table=table, winners=winners, losers=losers, a=len(table), user_id=session["user_id"])


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/schedule", methods=["GET", "POST"])
@login_required
def schedule():
    if request.method == "POST":
        # Get all inputs and put them into a string
        schedule = ''
        for i in range(2):
            for j in range(5):
                if request.form.get(str(i + 1) + str(j + 1)):
                    schedule = schedule + '1'
                else:
                    schedule = schedule + '0'
        # Modify database
        db.execute("UPDATE users SET schedule=:schedule WHERE id=:user_id", schedule=schedule, user_id=session["user_id"])

        return redirect("/schedule")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Get schedule list
        schedule = []
        schedule.append([]) # Morning
        schedule.append([]) # Evening
        sschedule = db.execute("SELECT schedule FROM users WHERE id = :user_id", user_id=session["user_id"])
        i = 0
        j = 0
        for char in sschedule[0]["schedule"]: # Has exactly 10 chars which will be '0' or '1'
            schedule[i].append(int(char))
            j += 1
            if j == 5:
                i += 1
        return render_template("schedule.html", schedule=schedule)


@app.route("/find", methods=["GET", "POST"])
@login_required
def find():
    if request.method == "POST":
        # Check if it is search by username --- TYPE = 1
        if request.form.get("username"):
            username = request.form.get("username")
            # Find in the database
            information = db.execute("SELECT username, email, schedule FROM users WHERE username = :username", username=username)
            # If there were no matches
            if not information:
                return apology("That user is not registered!")
            else:
                # Get the number of games played agains that user
                # Get that user's id
                user_id = db.execute("SELECT id FROM users WHERE username = :username", username=username)
                games_lost = db.execute ("SELECT COUNT(match_id) FROM matches WHERE winner_id = :winner_id AND loser_id = :loser_id", winner_id=user_id[0]["id"], loser_id=session["user_id"])
                games_won = db.execute ("SELECT COUNT(match_id) FROM matches WHERE winner_id = :winner_id AND loser_id = :loser_id", winner_id=session["user_id"], loser_id=user_id[0]["id"])
                # Get that user's schedule and put it into a list
                schedule = []
                schedule.append([]) # Morning
                schedule.append([]) # Evening
                sschedule = db.execute("SELECT schedule FROM users WHERE id = :user_id", user_id=session["user_id"])
                i = 0
                j = 0
                for char in sschedule[0]["schedule"]: # Has exactly 10 chars which will be '0' or '1'
                    schedule[i].append(int(char))
                    j += 1
                    if j == 5:
                        i += 1
                return render_template("found.html", information=information, TYPE=1, games_won=games_won[0]["COUNT(match_id)"], games_lost=games_lost[0]["COUNT(match_id)"], games_played=games_won[0]["COUNT(match_id)"] + games_lost[0]["COUNT(match_id)"], schedule=schedule)
        # Request was made by schedule --- TYPE = 2
        else:
            # Get all inputs and put them into a list
            timeframes = []
            for i in range(2):
                for j in range(5):
                    if request.form.get(str(i + 1) + str(j + 1)):
                        timeframes.append(1)
                    else:
                        timeframes.append(0)
            # Make the final list to pass
            definitivelist = []
            for i in range(10): # For the 10 timeframes
                # Create the list to append
                list = []
                # Check if it was chosen to be shown
                if timeframes[i] == 0:
                    list.append(0)
                # If it was chosen to be shown
                else:
                    list.append(1)
                    # Get the information
                    raw_information = db.execute("SELECT username, email, schedule, id FROM users")
                    # Process to keep only the ones where the schedule matches
                    information = []
                    for dictionary in raw_information:
                        if dictionary["schedule"][i] == '1':
                            extralist = []
                            extralist.append(dictionary["username"])
                            extralist.append(dictionary["email"])
                            # If the user is different from the logged in one
                            if dictionary["id"] != session["user_id"]:
                                information.append(extralist)
                    if not information:
                        list.append(0)
                        list.append(0)
                    else:
                        list.append(1)
                        list.append(information)
                definitivelist.append(list)
            # For each list in definitivelist append the name of the timeframe
            i = 0
            j = 0
            for list in definitivelist:
                string = ''
                # Append day
                if j == 0 or j == 5:
                    string = string + "Monday"
                elif j == 1 or j == 6:
                    string = string + "Tuesday"
                elif j == 2 or j == 7:
                    string = string + "Wednesday"
                elif j == 3 or j == 8:
                    string = string + "Thursday"
                else:
                    string = string + "Friday"
                if i == 0:
                    string = string + ' ' + 'morning'
                else:
                    string = string + ' ' + 'evening'
                j += 1
                if j == 5:
                    i += 1
                list.append(string)
            return render_template("found.html", definitivelist=definitivelist, TYPE=2)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        # Get schedule list
        schedule = []
        schedule.append([]) # Morning
        schedule.append([]) # Evening
        sschedule = db.execute("SELECT schedule FROM users WHERE id = :user_id", user_id=session["user_id"])
        i = 0
        j = 0
        for char in sschedule[0]["schedule"]: # Has exactly 10 chars which will be '0' or '1'
            schedule[i].append(int(char))
            j += 1
            if j == 5:
                i += 1
        return render_template("find.html", schedule=schedule)


@app.route("/register", methods=["GET", "POST"])
def register():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password1"):
            return apology("must provide password", 403)

        # Ensure email was submitted
        elif not request.form.get("email1"):
            return apology("must provide email", 403)

        # Check if username is available
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(rows) != 0:
            return apology("username already taken", 403)

        # Check password validity
        if len(request.form.get("password1")) < 8:
            return apology("password too short!", 403)
        if request.form.get("password1") != request.form.get("password2"):
            return apology("password must match repeat!", 403)
        letters = 0
        numbers = 0
        for char in request.form.get("password1"):
            if char.isalpha():
                letters += 1
            elif char.isdigit():
                numbers += 1
        if letters < 1 and numbers < 1:
            return apology("Invalid password", 403)

        #Check email
        at = False
        for character in request.form.get("email1"):
            if character == '@':
                at = True
        if not at:
            return apology("invalid email", 403)
        if request.form.get("email1") != request.form.get("email2"):
            return apology("email must match repeat!", 403)

        # Insert into database
        db.execute("INSERT INTO users (username, hash, email, schedule) VALUES(:username, :hashed, :email, '0000000000')", username=request.form.get("username"), hashed=generate_password_hash(request.form.get("password1")), email=request.form.get("email1"))

        # Remember which user has logged in
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    # Method is post
    else:
        winner = request.form.get("winner")
        loser = request.form.get("loser")
        wpoints = request.form.get("wpoints")
        lpoints = request.form.get("lpoints")
        # Check if usernames are valid
        winnerdata = db.execute("SELECT username, id FROM users WHERE username = :username", username = winner)
        loserdata = db.execute("SELECT username, id FROM users WHERE username = :username", username = loser)
        if not winnerdata or not loserdata:
            return apology("invalid usernames")
        if winner != winnerdata[0]["username"]:
            return apology("winner not registered")
        elif loser != loserdata[0]["username"]:
            return apology("loser not registered")
        # Check winner and loser are different
        if winner == loser:
            return apology("winner and loser must be different people!")
        # Check if logged in person played in the match
        if session["user_id"] != winnerdata[0]["id"] and session["user_id"] != loserdata[0]["id"]:
            return apology("Players must register their own games!")
        # Check if scores are valid
        if (int(wpoints) - int(lpoints)) < 2:
            return apology("Invalid score")
        # Insert into database
        db.execute("INSERT INTO matches (winner_id, loser_id, points_winner, points_loser, date) VALUES (:winner_id, :loser_id, :pwinner, :ploser, :date)",
            winner_id = winnerdata[0]["id"],
            loser_id = loserdata[0]["id"],
            pwinner = wpoints,
            ploser = lpoints,
            date = request.form.get("date")
            )
        return redirect("/matches")


@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    if request.method == "GET":
        return render_template("remove.html")
    # Method is post
    else:
        match = request.form.get("match_id")
        # Check if user was in that match
        information = db.execute("SELECT winner_id, loser_id FROM matches WHERE match_id = :match_id", match_id = match)
        if not information:
            return apology("Invalid match id. Maybe you havent played any matches yet")
        if information[0]["winner_id"] != session["user_id"] and information[0]["loser_id"] != session["user_id"]:
            return apology("Match must be removed by the players")
        # Remove from database
        db.execute("DELETE FROM matches WHERE match_id = :match_id", match_id = match)
        return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)