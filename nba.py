from flask import Flask, render_template, url_for, redirect
import requests
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap(app)

player_endpoint = 'https://www.balldontlie.io/api/v1/players/'
team_endpoint = 'https://www.balldontlie.io/api/v1/teams/'
game_endpoint = 'https://www.balldontlie.io/api/v1/games/'

#Player Form
class PlayerSearch(FlaskForm):
    player_id = StringField('Player ID', validators=[DataRequired()])
    submit = SubmitField('Search')

#Team Form
class TeamSearch(FlaskForm):
    team_id = StringField('Team ID', validators=[DataRequired()])
    submit = SubmitField('Search')

@app.route('/', methods=['GET', 'POST'])
def index():
    player_form = PlayerSearch()
    team_form = TeamSearch()

    if player_form.validate_on_submit():
        player_id = player_form.player_id.data
        return redirect(url_for('player_info', player_id=player_id))
    
    if team_form.validate_on_submit():
        team_id = team_form.team_id.data
        return redirect(url_for('team_info', team_id=team_id))
    
    game_id = random.randint(10, 9999)
    try:
        url = game_endpoint + str(game_id)
        r = requests.get(url)
        game_data = r.json()
    except:
        game_data = None

    return render_template('index.html', player_form=player_form, team_form=team_form, game_data=game_data)

#Route to player_info.html
@app.route('/player/<player_id>')
def player_info(player_id):
    try:
        url = player_endpoint + str(player_id)
        r = requests.get(url)
        data = r.json()
        print(data)
    except:
        print('Please try again')

    return render_template('player_info.html', data=data)

#Route to team_info.html
@app.route('/team/<team_id>')
def team_info(team_id):
    try:
        url = team_endpoint + str(team_id)
        r = requests.get(url)
        data = r.json()
        print(data)
    except:
        print('Please try again')

    return render_template('team_info.html', data=data)

#Random player
@app.route('/player')
def player():
    try:
        player_id = random.randint(1,500)
        url = player_endpoint + str(player_id)
        r = requests.get(url)
        data = r.json()
        print(data)
    except:
        print('Please try again')

    return render_template('player_info.html', data=data)

#View teams
@app.route('/teams')
def teams():
    return render_template('view_teams.html')

if __name__ == '__index__':
    app.run()
