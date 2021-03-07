import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    # Method can only by GET
    # Get the stocks that were bought and sold by the user
    bought = db.execute("SELECT symbol, name, SUM(amount) FROM history WHERE user_id=:user_id AND type='BUY' GROUP BY symbol", user_id=session["user_id"])
    sold = db.execute("SELECT symbol, SUM(amount) FROM history WHERE user_id=:user_id AND type='SELL' GROUP BY symbol", user_id=session["user_id"])
    # For each company that has been sold, update bought to leave only remaining number of shares
    for dictionary in sold:
        # Get the symbol
        symbol = dictionary["symbol"]
        # Iterate bought until that symbol is found
        for item in bought:
            if item["symbol"] == symbol:
                # Update the amount of shares
                item["SUM(amount)"] = item["SUM(amount)"] - dictionary["SUM(amount)"]
                break
    # Get current cash
    current_cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
    total = 0.0
    # Make a list to pass to display.html
    table = []
    for dictionary in bought:
        # Get current price of each stock
        information = lookup(dictionary["symbol"])
        current_price = information["price"]
        # Append the dictionary with information into the list table only if user has tocks
        if dictionary["SUM(amount)"] > 0:
            table.append({
                "symbol": dictionary["symbol"],
                "name": dictionary["name"],
                "shares": dictionary["SUM(amount)"],
                "price": float("{:.2f}".format(current_price)),
                "total": float("{:.2f}".format((dictionary["SUM(amount)"]) * current_price))
            })
            total += ((dictionary["SUM(amount)"]) * current_price)

    total += current_cash[0]["cash"]
    return render_template("index.html", table=table, cash=float("{:.2f}".format(current_cash[0]["cash"])), total=float("{:.2f}".format(total)))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # Get symbol and check if its valid
        information = lookup(request.form.get("symbol"))
        # If invalid stock symbol, information was given None
        if not information:
            return apology("Invalid stock symbol")
        # Check number of shares
        if int(request.form.get("shares")) < 1:
            return apology("Invalid number of shares")
        # Get cash available
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])
        # Check amount bought
        if cash[0]["cash"] < (int(request.form.get("shares")) * information["price"]):
            return apology("Dont have enough money")
        # Register the buying
        user_id=session["user_id"],
        price=information["price"],
        amount=int(request.form.get("shares")),
        symbol=information["symbol"],
        name=information["name"],
        db.execute("INSERT INTO history (user_id, price, amount, time, symbol, name, type) VALUES (:user_id, :price, :amount, datetime('now'), :symbol, :name, 'BUY')",
            user_id=user_id,
            price=price,
            amount=amount,
            symbol=symbol,
            name=name,
            )
        # Change the cash
        db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=cash[0]["cash"] - (int(request.form.get("shares")) * information["price"]), user_id=session["user_id"])
        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    table = db.execute("SELECT symbol, price, amount, time, type FROM history WHERE user_id=:user_id", user_id=session["user_id"])
    if not table:
        return apology("You didnt make operations yet")
    else:
        #Modify table so price has two decimal digits
        for dictionary in table:
            dictionary["price"] = float("{:.2f}".format(dictionary["price"]))
        return render_template("history.html", table=table)


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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        #Get the info for the stock
        information = lookup(request.form.get("symbol"))
        #If invalid stock symbol, information was given None
        if not information:
            return apology("Invalid stock symbol")
        #If received correctly, show information
        else:
            return render_template("quoted.html", company=information["name"], symbol=information["symbol"], price=float("{:.2f}".format(information["price"])))

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
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
        if len(rows) != 0:
            return apology("username already taken", 403)

        if (request.form.get("password")) == '':
            return apology("invalid password", 403)
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("invalid password", 403)

        # Insert into database
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :hashed)", username=request.form.get("username"), hashed=generate_password_hash(request.form.get("password")))

        # Remember which user has logged in
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        symbols = []
        #Get the list of companies where the user has stocks
        # Get the stocks that were bought and sold by the user
        bought = db.execute("SELECT symbol, SUM(amount) FROM history WHERE user_id=:user_id AND type='BUY' GROUP BY symbol", user_id=session["user_id"])
        sold = db.execute("SELECT symbol, SUM(amount) FROM history WHERE user_id=:user_id AND type='SELL' GROUP BY symbol", user_id=session["user_id"])
        # For each company that has been sold, update bought to leave only remaining number of shares
        for dictionary in sold:
            # Get the symbol
            symbol = dictionary["symbol"]
            # Iterate bought until that symbol is found
            for item in bought:
                if item["symbol"] == symbol:
                    # Update the amount of shares
                    item["SUM(amount)"] = item["SUM(amount)"] - dictionary["SUM(amount)"]
                    break
        for dictionary in bought:
            if dictionary["SUM(amount)"] != 0:
                symbols.append(dictionary["symbol"])
        return render_template("sell.html", symbols=symbols)
    #If method is POST
    else:
        # Check it is valid
        # Request exists
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("Invalid request")
        # Number of shares is positive
        if int(request.form.get("shares")) <= 0:
            return apology("Invalid number of shares")
        # User has enough shares
        # Get number of shares for that company
        sharesbought = db.execute("SELECT SUM(amount) FROM history WHERE user_id=:user_id AND symbol=:symbol AND type='BUY'", user_id=session["user_id"], symbol=request.form.get("symbol"))
        sharessold = db.execute("SELECT SUM(amount) FROM history WHERE user_id=:user_id AND symbol=:symbol AND type='SELL'", user_id=session["user_id"], symbol=request.form.get("symbol"))
        if sharessold[0]["SUM(amount)"]:
            shares = sharesbought[0]["SUM(amount)"] - sharessold[0]["SUM(amount)"]
        else:
            shares = sharesbought[0]["SUM(amount)"]

        if int(request.form.get("shares")) > shares:
            return apology("Dont have that many shares!")

        # If it is valid
        # Get the current price
        information = lookup(request.form.get("symbol"))
        # Update user's history
        user_id=session["user_id"],
        price=information["price"],
        amount=int(request.form.get("shares")),
        symbol=information["symbol"],
        name=information["name"],
        db.execute("INSERT INTO history (user_id, price, amount, time, symbol, name, type) VALUES (:user_id, :price, :amount, datetime('now'), :symbol, :name, 'SELL')",
            user_id=user_id,
            price=price,
            amount=amount,
            symbol=symbol,
            name=name
            )
        # Update user's cash
        # Get the users current cash
        cashh = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=user_id)
        print(cashh[0]["cash"])
        print(amount)
        print(price)
        cash = cashh[0]["cash"] + (int(request.form.get("shares")) * information["price"])
        #Update
        db.execute("UPDATE users SET cash=:cash WHERE id=:user_id", cash=cash, user_id=user_id)

        return redirect("/")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        # Get current cash
        current_cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
        return render_template("add.html", cash=float("{:.2f}".format(current_cash[0]["cash"])))
    # Method is post
    else:
        # Check the amount is positive
        if float(request.form.get("cash")) <= 0:
            return apology("Invalid amount of money!")
        # Get the current cash
        current_cash = db.execute("SELECT cash FROM users WHERE id=:user_id", user_id=session["user_id"])
        cash = current_cash[0]["cash"]
        # If wanting to add
        if request.form.get("action") == "Add":
            # Add the amount to the account
            db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",
                cash=cash + float(request.form.get("cash")),
                user_id=session["user_id"])
            # Register operation
            db.execute("INSERT INTO history (user_id, price, amount, time, symbol, name, type) VALUES (:user_id, :price, NULL, datetime('now'), NULL, NULL, 'ADD')",
                user_id = session["user_id"],
                price=float(request.form.get("cash")))
            return redirect("/")
        #If wanting to retrieve
        else:
            #Check if it has enough cash
            if cash < float(request.form.get("cash")):
                return apology("Don't have enough cash!")
            else:
                #Substract the amount from the account
                db.execute("UPDATE users SET cash=:cash WHERE id=:user_id",
                    cash=cash - float(request.form.get("cash")),
                    user_id=session["user_id"])
                # Register operation
                db.execute("INSERT INTO history (user_id, price, amount, time, symbol, name, type) VALUES (:user_id, :price, NULL, datetime('now'), NULL, NULL, 'RETRIEVE')",
                    user_id = session["user_id"],
                    price=float(request.form.get("cash")),
                    )
                return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
