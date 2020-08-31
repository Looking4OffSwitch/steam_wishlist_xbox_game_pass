# from steam import get_steam_wishlist_game_names
# from xbox import get_xbox_game_pass_game_names
# from utils import degree_difference
#
# # STEAM_API_KEY = "C1F1009856FE1DB295B3002453AFFF33"
# # DUSTINS_STEAMID = "76561197968568357"
# REEDS_STEAMID = "76561198025135548"
#
#
# def wishlist_games_available_on_game_pass(steamid: str):
#     wishlist_game_names = get_steam_wishlist_game_names(REEDS_STEAMID)
#     xbox_game_pass_game_names = get_xbox_game_pass_game_names()
#
#     for name1 in wishlist_game_names:
#         for name2 in xbox_game_pass_game_names:
#             if (degree_difference(name1, name2) <= max_levenshtein_dist):
#                 games.append(name1)
#
#     return games
#
# # def wishlist_games_available_on_game_passX(steamid: str, max_levenshtein_dist: int = 2):
# #     games = []
# #
# #     wishlist_game_names = get_steam_wishlist_game_names(REEDS_STEAMID)
# #     xbox_game_pass_game_names = get_xbox_game_pass_game_names()
# #
# #     for name1 in wishlist_game_names:
# #         for name2 in xbox_game_pass_game_names:
# #             if (degree_difference(name1, name2) <= max_levenshtein_dist):
# #                 games.append(name1)
# #
# #     return games
# #
# #
# # def main():
# #     wishlist_game_names = get_steam_wishlist_game_names(REEDS_STEAMID)
# #     # print('\n'.join(wishlist_game_names))
# #     # print(wishlist_game_names)
# #
# #     # print('-' * 80)
# #
# #     xbox_game_pass_game_names = get_xbox_game_pass_game_names()
# #     # print('\n'.join(xbox_game_pass_game_names))
# #     # print(xbox_game_pass_game_names)
# #
# #     available_games = wishlist_games_available_on_game_pass(wishlist_game_names,
# #                                                             xbox_game_pass_game_names)
# #     print('\n'.join(available_games))
# #
# #
# # if __name__ == '__main__':
# #     main()
