from flask.templating import render_template
from app import app
from modules import game
from modules import player

@app.route('/rps')
def index():
    return render_template('base.html')
    

@app.route('/rps/play/<choice_1>/<choice_2>')
def play(choice_1,choice_2):
    return f"The winner is {game.play(choice_1,choice_2)}"

