from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
import sqlite3

app = Flask(__name__)


# conn = sqlite3.connect('froshims.db')
# cur = conn.cursor()

REGISTRANTS = {}

SPORTS = ["Dodgeball", 
          "Flag Football", 
          "Soccer", 
          "Volleyball", 
          "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=['POST'])
def register():
    name = request.form.get("name")
    if not name: 
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    #cur.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", name, sport)
    
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    #registrants = cur.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=REGISTRANTS)