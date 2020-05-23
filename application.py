from cs50 import SQL
from flask import Flask, render_template, request, redirect, flash
from werkzeug.exceptions import default_exceptions

from helpers import apology

app = Flask(__name__)
#secret key for error message generation in apology
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#connect the database
db = SQL("sqlite:///kickeridoo.db")

@app.route("/")
def index():
    #just render the main page
    return render_template("index.html")

@app.route("/add-result")
def add_result():

    players = db.execute("SELECT id, name FROM players ORDER BY name ASC")

    return render_template("add-result.html", players=players) 

@app.route("/t1-win")
def t1_win():

    flash("T1 added!")
    return redirect("/add-result")

@app.route("/draw")
def draw():

    flash("Draw added!")
    return redirect("/add-result")

@app.route("/t2-win")
def t2_win():

    flash("T2 added!")
    return redirect("/add-result")

@app.route("/add-player", methods=["GET", "POST"])
def player_list():

    if request.method == "POST":
        #obtain the name from the form
        name = request.form.get("player_name")
        #insert the name into the database
        db.execute("INSERT INTO players (name) VALUES(:name)", name=name)
        #flash a message if successful
        flash("Player added!")
        #redirect to the same page again
        return redirect("/add-player")

    #just load the page when access without inserting name
    return render_template("add-player.html")

@app.route("/player-ranking")
def player_ranking():

    #select all data from the player
    players = db.execute("SELECT * FROM players ORDER BY name ASC")

    #render the page with the result of obtained
    return render_template("player-ranking.html", players=players)  

@app.route("/team-ranking")
def team_ranking():

    #select the information required for the team ranking
    teams = db.execute("SELECT p1.name as p1_name, p2.name as p2_name, teams.w, teams.d, teams.l FROM teams JOIN players p1 on teams.p1_id = p1.id JOIN players p2 on teams.p2_id = p2.id;")

    #render the page with the team information
    return render_template("team-ranking.html", teams=teams)    

def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)

# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
