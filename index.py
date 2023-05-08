from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests

app = Flask(__name__)
bootstrap = Bootstrap5(app)

endpoint = 'https://www.balldontlie.io/api/v1/players/'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/player')
def player():
    try:
        player_id = 100
        url = endpoint + str(player_id)
        r = requests.get(url)
        data = r.json()
        print(data)
    except:
        print('Please try again')

    return render_template('player.html', data=data)

if __name__ == '__main__':
    app.run()