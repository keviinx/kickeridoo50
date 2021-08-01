from cs50 import SQL
from flask import Flask, render_template, request, redirect, flash
from werkzeug.exceptions import default_exceptions
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from threading import Timer
import sys

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
            update_player_result("w",t1p1)
            update_player_result("l",t2p1)
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
            t1order = reorder_team(t1p1,t1p2)
            t2order = reorder_team(t2p1,t2p2)
            #check if any team already created
            t1teamcheck = team_exist_check(t1order[0]['id'], t1order[1]['id'])
            t2teamcheck = team_exist_check(t2order[0]['id'], t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                insert_team("w", t1order[0]['id'], t1order[1]['id'])
                update_player_result("w",t1order[0]['id'])
                update_player_result("w",t1order[1]['id'])
            #if found
            else:
                update_team_result("w", t1order[0]['id'], t1order[1]['id'])
                update_player_result("w",t1order[0]['id'])
                update_player_result("w",t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                insert_team("l", t2order[0]['id'], t2order[1]['id'])
                update_player_result("l",t2order[0]['id'])
                update_player_result("l",t2order[1]['id'])
            #if found
            else:
                update_team_result("l", t2order[0]['id'], t2order[1]['id'])
                update_player_result("l",t2order[0]['id'])
                update_player_result("l",t2order[1]['id'])
              
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
            update_player_result("d",t1p1)
            update_player_result("d",t2p1)
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
            t1order = reorder_team(t1p1,t1p2)
            t2order = reorder_team(t2p1,t2p2)
            #check if any team already created
            t1teamcheck = team_exist_check(t1order[0]['id'], t1order[1]['id'])
            t2teamcheck = team_exist_check(t2order[0]['id'], t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                insert_team("d", t1order[0]['id'], t1order[1]['id'])
                update_player_result("d",t1order[0]['id'])
                update_player_result("d",t1order[1]['id'])
            #if found
            else:
                update_team_result("d", t1order[0]['id'], t1order[1]['id'])
                update_player_result("d",t1order[0]['id'])
                update_player_result("d",t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                insert_team("d", t2order[0]['id'], t2order[1]['id'])
                update_player_result("d",t2order[0]['id'])
                update_player_result("d",t2order[1]['id'])
            #if found
            else:
                update_team_result("d", t2order[0]['id'], t2order[1]['id'])
                update_player_result("d",t2order[0]['id'])
                update_player_result("d",t2order[1]['id'])
              
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
            update_player_result("l",t1p1)
            update_player_result("w",t2p1)
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
            t1order = reorder_team(t1p1,t1p2)
            t2order = reorder_team(t2p1,t2p2)
            #check if any team already created
            t1teamcheck = team_exist_check(t1order[0]['id'], t1order[1]['id'])
            t2teamcheck = team_exist_check(t2order[0]['id'], t2order[1]['id'])
            #team 1 check
            #if not found
            if len(t1teamcheck) == 0:
                insert_team("l", t1order[0]['id'], t1order[1]['id'])
                update_player_result("l",t1order[0]['id'])
                update_player_result("l",t1order[1]['id'])
            #if found
            else:
                update_team_result("l", t1order[0]['id'], t1order[1]['id'])
                update_player_result("l",t1order[0]['id'])
                update_player_result("l",t1order[1]['id'])
            #team 2 check
            # if not found
            if len(t2teamcheck) == 0:
                insert_team("w", t2order[0]['id'], t2order[1]['id'])
                update_player_result("w",t2order[0]['id'])
                update_player_result("w",t2order[1]['id'])
            #if found
            else:
                update_team_result("w", t2order[0]['id'], t2order[1]['id'])
                update_player_result("w",t2order[0]['id'])
                update_player_result("w",t2order[1]['id'])
              
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

#function for updating player result
def update_player_result(result, id):
    if result == "w":
        db.execute("UPDATE players SET w = w + 1 WHERE id = (:id)", id=id)
    elif result == "d":
        db.execute("UPDATE players SET d = d + 1 WHERE id = (:id)", id=id)
    else:
        db.execute("UPDATE players SET l = l + 1 WHERE id = (:id)", id=id)

#function for rearranging player alphabetically
def reorder_team(player1id, player2id):
    return db.execute("SELECT id FROM players WHERE id = (:player1id) OR id = (:player2id) ORDER BY name ASC", player1id=player1id, player2id=player2id)

#function for checking if the team already exist
def team_exist_check(player1id, player2id):
    return db.execute("SELECT * FROM teams WHERE p1_id = :player1id AND p2_id = :player2id", player1id=player1id, player2id=player2id)

#function for inserting new team into db
def insert_team(result, player1id, player2id):
    db.execute("INSERT INTO teams (p1_id, p2_id, :result) VALUES ((:player1id),(:player2id),1)", player1id=player1id, player2id=player2id, result=result)

# function for updating team result
def update_team_result(result, player1id, player2id):
    if result == "w":
        db.execute("UPDATE teams SET w = w + 1 WHERE p1_id = (:player1id) AND p2_id = (:player2id)", player1id=player1id, player2id=player2id)
    elif result == "d":
        db.execute("UPDATE teams SET d = d + 1 WHERE p1_id = (:player1id) AND p2_id = (:player2id)", player1id=player1id, player2id=player2id)
    else:
        db.execute("UPDATE teams SET l = l + 1 WHERE p1_id = (:player1id) AND p2_id = (:player2id)", player1id=player1id, player2id=player2id)


# Define function for QtWebEngine
def ui(location):
    qt_app = QApplication(sys.argv)

    web = QWebEngineView()
    web.setWindowIcon(QtGui.QIcon('./static/favicon.ico'))
    web.setWindowTitle("Kickeridoo50")
    web.resize(800, 600)
    #web.setZoomFactor(1.5)
    web.load(QUrl(location))
    web.show()

    sys.exit(qt_app.exec_())


if __name__ == "__main__":
    # start sub-thread to open the browser.
    Timer(1, lambda: ui("http://127.0.0.1:5000/")).start()
    app.run()
