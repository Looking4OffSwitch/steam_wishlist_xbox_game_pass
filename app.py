from flask import Flasks
from main import wishlist_games_available_on_game_pass

app = Flask(__name__)

REEDS_STEAMID = "76561198025135548"

@app.route('/')
def home():
    # games = wishlist_games_available_on_game_pass(REEDS_STEAMID)
    return '\n'.join('many', 'games'])
    #return '\n'.join(games)


if __name__ == '__main__':
    app.run()
