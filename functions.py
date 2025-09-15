import pygame as pg
from colors import RED
import importlib.util
import sys
import os
import json

def level_reset(level):
    level = my_import(level)
    level.text = level.original_text[::]
    level.cards = [i[::] for i in level.original_cards]
    level.did_actions = 0


def game_reset(list_of_levels):
    map(lambda x: level_reset(my_import(x)), list_of_levels)


def check_money(game_data, card):
    if "money" in card:
        if "random" in card and game_data["money"] == 0:
            return False
        elif game_data["money"] + int(card[card.index("money") + 1]) < 0:
            return False
    return True


def draw_heart(surface, x, y):
    pg.draw.ellipse(surface, RED, (x - 10, y - 15, 18, 25))
    pg.draw.ellipse(surface, RED, (x + 5, y - 15, 18, 25))
    pg.draw.polygon(surface, RED, ((x - 10, y), (x + 6, y + 22), (x + 22, y)))



def my_import(file_name):

    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_path, "levels")
    file_path = os.path.join(path, file_name + ".py")

    spec = importlib.util.spec_from_file_location(file_name, file_path)

    level = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(level)
    return level


def check_hearts(game_data):
    if game_data["hearts"] > 0:
        return True
    else:
        return False


def create_game_data():
    return {
        "hearts": 3,
        "level": "level0",
        "scene": 0,
        "know_band": 0,
        "know_place_band": 0,
        "money": 0,
        "distrust": 0,
        "imposter_killed": 0,
        "cartridges": 0,
        "rifle": 0,
        "dynamit": 0,
        "know_imposter": 0,
        "scorpions_caught": 0,
        "imposter_caught": 0,
        "fox_killed": 0,
        "fox_caught": 0,
        "resque_sheriff": 0
    }
def create_configuration():
    return {
        "volume": "50"
    }
def save_stats(stats, stats_path):
    try:
        with open(stats_path, "w") as file:
            json.dump(stats, file, indent=4)
    except Exception as e:
        print(e)


def load_stats(file_name, feature, app_name):
    path = get_appdata_path(app_name)
    if not os.path.exists(path):
        os.makedirs(path)
    stats_path = os.path.join(path, file_name)
    if not os.path.exists(stats_path):
        default_stats = feature()
        save_stats(default_stats, stats_path)
        return default_stats
    try:
        with open(stats_path, "r") as file:
            stats = json.load(file)
        return stats
    except:
        return feature()


def get_path(file_name):
    if file_name.endswith(".jpg"):
        directory = "pictures"
    elif file_name.endswith(".wav") or file_name.endswith(".mp3"):
        directory = "sounds"
    return os.path.join(os.path.join(getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__))), directory), file_name)


def get_appdata_path(appname):
    if sys.platform == "win32":
        return os.path.join(os.environ['APPDATA'], appname)
    elif sys.platform == "darwin":
        return os.path.join(os.path.expanduser("~"), "Library", "Application Support", appname)
    else:
        return os.path.join(os.path.expanduser("~"), ".local", "share", appname)