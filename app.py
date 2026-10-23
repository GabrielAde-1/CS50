import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to our newly created wishlist database
db = SQL("sqlite:///wishlist.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached by the browser"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve input elements from the frontend form
        name = request.form.get("name")
        item = request.form.get("item")
        event = request.form.get("event")

        # Basic verification check to stop empty entries
        if not name or not item or not event:
            return redirect("/")

        # Record entry directly to SQLite table grid
        db.execute(
            "INSERT INTO wishlist (name, item, event) VALUES (?, ?, ?)",
            name, item, event
        )
        return redirect("/")

    else:
        # Load all rows out of the database to populate the HTML grid
        saved_wishes = db.execute("SELECT * FROM wishlist")
        return render_template("index.html", wishes=saved_wishes)

@app.route("/delete", methods=["POST"])
def delete():
    """Allows users to drop a wish row entry out of the list grid"""
    item_id = request.form.get("id")
    if item_id:
        db.execute("DELETE FROM wishlist WHERE id = ?", item_id)
    return redirect("/")
