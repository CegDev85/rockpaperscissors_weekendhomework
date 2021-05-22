from flask.templating import render_template
from app import app
from modules import game
from modules import player

@app.route('/rps')
def index():
    return render_template('base.html')

@app.route('/rps/play')
def name_entry():
    return render_template('new_game.html')

@app.route('/rps/play/rules')
def game_rules():
    return render_template('how-to-play.html')

@app.route()


@app.route('/rps/play/<choice_1>/<choice_2>')
def play(choice_1,choice_2):
    return f"The winner is {game.play(choice_1,choice_2)}"

