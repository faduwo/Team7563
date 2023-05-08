from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

endpoint = 'https://www.balldontlie.io/api/v1/players/'

@app.route('/')
def main():
    try:
        player_id = 237
        url = endpoint + str(player_id)
        r = requests.get(url)
        data = r.json()
        print(data)
    except:
        print('Please try again')

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
