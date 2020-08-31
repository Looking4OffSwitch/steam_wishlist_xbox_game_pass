import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from utils import clean_string


def get_steam_wishlist_game_names(steamid: str, sort: bool = True):
    url = f"https://store.steampowered.com/wishlist/profiles/{steamid}/wishlistdata/"

    game_names = []

    try:
        response = requests.get(url)
        response.raise_for_status()

        wishlist_infos = response.json()

        # Looks like: {'244850': {'name': 'Space Engineers', 'capsule': ...
        # print(wishlist_infos)

        for key in wishlist_infos.keys():
            # print(wishlist_infos[key]['name'])
            name = wishlist_infos[key]['name']
            name = clean_string(name)
            game_names.append(name)

    except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError) as e:
        print("ERROR: get_steam_wishlist_game_names(...)")
        print(str(e))

    if (sort):
        game_names.sort()

    return game_names
