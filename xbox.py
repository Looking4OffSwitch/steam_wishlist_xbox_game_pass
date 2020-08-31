import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from utils import clean_string
# import json

# The game pass store page adds the following strings to some titles. We'll remove them if present.
# The strings are sorted in descending order by length so that the longest string is removed from a name first
extraneous_trailing_strings = sorted(['windows', 'windows 10', 'for windows 10', 'microsoft store edition', 'win10', 'pc', 'game preview'], key=len, reverse=True)
# print(extraneous_trailing_strings)


def get_xbox_game_pass_game_names(sort: bool = True):
    # headers = {'User-Agent': 'User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'}
    # Determined from: https://www.xbox.com/en-US/xbox-game-pass/games?=pcgames
    game_ids_url = 'https://catalog.gamepass.com/sigls/v2?id=fdd9e2a7-0fee-49f6-ad69-4354098401ff&language=en-us&market=US'
    game_info_url = 'https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds={}&market=US&languages=en-us&MS-CV=XXX'

    try:
        game_ids = requests.get(game_ids_url).json()
        s = ','.join(i['id'] for i in game_ids if 'id' in i)

        data = requests.get(game_info_url.format(s)).json()

        game_names = []

        for p in data['Products']:
            # print(json.dumps(p['LocalizedProperties'][0], sort_keys=True, indent=4))

            name = p['LocalizedProperties'][0]['ProductTitle']

            name = clean_string(name)

            for word in extraneous_trailing_strings:
                if (name.endswith(word)):
                    name = name.replace(word, '')
                    break

            # if (name.startswith('yakuza kiwami 2')):
            #    print(json.dumps(p, sort_keys=True, indent=4))

            game_names.append(name)

        # print some data to screen:
        # for p in data['Products']:
        #     print(p['LocalizedProperties'][0]['ProductTitle'])
        #     print(p['LocalizedProperties'][0]['ShortTitle'])
        #     print(p['LocalizedProperties'][0]['ShortDescription'])
        #     print('-' * 80)

    except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError) as e:
        print("ERROR: get_xbox_game_pass_game_names(...)")
        print(str(e))

    if (sort):
        game_names.sort()

    return game_names
