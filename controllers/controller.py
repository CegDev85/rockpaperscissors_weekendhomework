from app import app
from modules import game
from modules import player

@app.route('/')
def index():
    return "Are you ready to play?"

@app.route('/play/<choice_1>/<choice_2>')
def play(choice_1,choice_2):
    return f"The winner is {game.play(choice_1,choice_2)}"

