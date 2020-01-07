import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google-cloud.json'

from flask_app.user import User
from flask_app.player import Player


def users():
    with open('source_data/members.json') as file:
        user_list: list = json.load(file)
    for index, user_dict in enumerate(user_list):
        User.create_from_dict(user_dict)
        print(f"{index + 1} of {len(user_list)} uploaded.")
    print(f'Upload complete - {len(user_list)} uploaded.')


def players():
    Player.objects.delete()
    print(f"Deleted all existing players")
    with open('source_data/players.json') as file:
        player_list: list = json.load(file)
    for index, player_dict in enumerate(player_list):
        Player.create_from_dict(player_dict)
        print(f"{index + 1} of {len(player_list)} uploaded.")
    print(f'Upload complete - {len(player_list)} uploaded.')
