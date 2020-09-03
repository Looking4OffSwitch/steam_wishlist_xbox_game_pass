#!/usr/bin/env python3
import argparse
import mailer
from steam import get_steam_wishlist_game_names
from xbox import get_xbox_game_pass_game_names
from utils import degree_difference


def wishlist_games_available_on_game_pass(steamid: str, max_levenshtein_dist: int = 2):
    games = []

    wishlist_game_names = get_steam_wishlist_game_names(steamid)
    xbox_game_pass_game_names = get_xbox_game_pass_game_names()

    for name1 in wishlist_game_names:
        for name2 in xbox_game_pass_game_names:
            if (degree_difference(name1, name2) <= max_levenshtein_dist):
                games.append(name1)

    return games


def send_email_of_games(games):

    if len(games) > 0:
        mailer = mailer.Emailer()
        sendTo = "reed@themanginos.com"
        emailSubject = ""

        emailSubject = "New Xbox Game Pass Game From Steam Wishlist"

        game_names = '\n'.join(games)

        mailer.sendmail(sendTo, emailSubject, game_names)
        print('email sent')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--steamid", help="Users Steam ID", type=str, required=True)
    args = parser.parse_args()

    if (args.steamid):
        available_games = wishlist_games_available_on_game_pass(args.steamid)
        print('\n'.join(available_games))
        send_email_of_games(available_games)
    else:
        print("No games available at this time")
