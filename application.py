from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

a = [[]]

@app.route("/")
def index():
    
    x = 3
    if "board" not in session:
        session["board"] =  [[None, None, None],[None, None, None, None], [None, None, None, None]]
        session["turn"] = "X"
    a = session["board"]

      

    return render_template("game.html", game=session["board"],turn=session["turn"])    

@app.route("/play/<int:row>/<int:col>/<string:turn>")
def play(row, col,turn):
    session["board"][row][col] = turn

    
    
    if turn == "0":
        session["turn"] = "x"
    else:
        session["turn"] = "0"  


    return redirect(url_for("index"))
