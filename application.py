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

@app.route("/t1-win", methods=["GET", "POST"])
def t1_win():

    if request.method == "POST":
        # game type was solo
        if request.form.get("match_type") == 'solo':
            # get both player's id
            t1p1 = request.form.get("t1p1")
            t2p1 = request.form.get("t2p1")
            #update data in database
            db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t1p1)
            db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t2p1)
            #flash message
            flash("Result added!")
        #game type was team    
        elif request.form.get("match_type") == 'team':
            # get all player's id
            t1p1 = request.form.get("t1p1")
            t1p2 = request.form.get("t1p2")
            t2p1 = request.form.get("t2p1")
            t2p2 = request.form.get("t2p2")
            #rearrange the id of the player alphabetically
            t1order = db.execute("SELECT id FROM players WHERE id = (:t1p1id) OR id = (:t1p2id) ORDER BY name ASC", t1p1id=t1p1, t1p2id=t1p2)
            t2order = db.execute("SELECT id FROM players WHERE id = (:t2p1id) OR id = (:t2p2id) ORDER BY name ASC", t2p1id=t2p1, t2p2id=t2p2)
            #check if any team already created
            t1teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t1p1id) AND p2_id = (:t1p2id)", t1p1id=t1order[0]['id'], t1p2id=t1order[1]['id'])
            t2teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t2p1id) AND p2_id = (:t2p2id)", t2p1id=t2order[0]['id'], t2p2id=t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, w) VALUES ((:p1_id),(:p2_id),(:w))", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'], w=1)
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET w = w + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, l) VALUES ((:p1_id),(:p2_id),(:l))", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'], l=1)
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t2order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET l = l + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t2order[1]['id'])
              
            flash("Result added!")
    
    return redirect("/add-result")

@app.route("/draw", methods=["GET", "POST"])
def draw():

    if request.method == "POST":
        # game type was solo
        if request.form.get("match_type") == 'solo':
            # get both player's id
            t1p1 = request.form.get("t1p1")
            t2p1 = request.form.get("t2p1")
            #update data in database
            db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t1p1)
            db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t2p1)
            #flash message
            flash("Result added!")
            
        #game type was team    
        elif request.form.get("match_type") == 'team':
            # get all player's id
            t1p1 = request.form.get("t1p1")
            t1p2 = request.form.get("t1p2")
            t2p1 = request.form.get("t2p1")
            t2p2 = request.form.get("t2p2")
            #rearrange the id of the player alphabetically
            t1order = db.execute("SELECT id FROM players WHERE id = (:t1p1id) OR id = (:t1p2id) ORDER BY name ASC", t1p1id=t1p1, t1p2id=t1p2)
            t2order = db.execute("SELECT id FROM players WHERE id = (:t2p1id) OR id = (:t2p2id) ORDER BY name ASC", t2p1id=t2p1, t2p2id=t2p2)
            #check if any team already created
            t1teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t1p1id) AND p2_id = (:t1p2id)", t1p1id=t1order[0]['id'], t1p2id=t1order[1]['id'])
            t2teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t2p1id) AND p2_id = (:t2p2id)", t2p1id=t2order[0]['id'], t2p2id=t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, d) VALUES ((:p1_id),(:p2_id),(:d))", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'], d=1)
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET d = d + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, d) VALUES ((:p1_id),(:p2_id),(:d))", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'], d=1)
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t2order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET d = d + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=t2order[1]['id'])
              
            flash("Result added!")

    return redirect("/add-result")

@app.route("/t2-win", methods=["GET", "POST"])
def t2_win():

    if request.method == "POST":
        # game type was solo
        if request.form.get("match_type") == 'solo':
            # get both player's id
            t1p1 = request.form.get("t1p1")
            t2p1 = request.form.get("t2p1")
            #update data in database
            db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t1p1)
            db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t2p1)
            #flash message
            flash("Result added!")
            
        #game type was team    
        elif request.form.get("match_type") == 'team':
            # get all player's id
            t1p1 = request.form.get("t1p1")
            t1p2 = request.form.get("t1p2")
            t2p1 = request.form.get("t2p1")
            t2p2 = request.form.get("t2p2")
            #rearrange the id of the player alphabetically
            t1order = db.execute("SELECT id FROM players WHERE id = (:t1p1id) OR id = (:t1p2id) ORDER BY name ASC", t1p1id=t1p1, t1p2id=t1p2)
            t2order = db.execute("SELECT id FROM players WHERE id = (:t2p1id) OR id = (:t2p2id) ORDER BY name ASC", t2p1id=t2p1, t2p2id=t2p2)
            #check if any team already created
            t1teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t1p1id) AND p2_id = (:t1p2id)", t1p1id=t1order[0]['id'], t1p2id=t1order[1]['id'])
            t2teamcheck = db.execute("SELECT * FROM teams WHERE p1_id = (:t2p1id) AND p2_id = (:t2p2id)", t2p1id=t2order[0]['id'], t2p2id=t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, l) VALUES ((:p1_id),(:p2_id),(:l))", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'], l=1)
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET l = l + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t1order[0]['id'], p2_id=t1order[1]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t1order[0]['id'])
                db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                db.execute("INSERT INTO teams (p1_id, p2_id, w) VALUES ((:p1_id),(:p2_id),(:w))", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'], w=1)
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t2order[1]['id'])
            #if found
            else:
                db.execute("UPDATE teams SET w = w + 1 WHERE p1_id = (:p1_id) AND p2_id = (:p2_id)", p1_id=t2order[0]['id'], p2_id=t2order[1]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t2order[0]['id'])
                db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=t2order[1]['id'])
              
            flash("Result added!")

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
    teams = db.execute("SELECT p1.name as p1_name, p2.name as p2_name, teams.w, teams.d, teams.l FROM teams JOIN players p1 on teams.p1_id = p1.id JOIN players p2 on teams.p2_id = p2.id ORDER BY p1_name ASC")

    #render the page with the team information
    return render_template("team-ranking.html", teams=teams)    

def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)

# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
