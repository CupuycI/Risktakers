import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path

background_img = pg.image.load(get_path("background_menu_of_dead.jpg"))
music = [pg.mixer.Sound(get_path("Death.mp3")), "death"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ["      Дикий запад суров      "]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "menu_of_dead"
next_level = "level0"
original_cards = [[[pg.image.load(get_path("card_menu_of_death.jpg")), pg.image.load(get_path("card_menu_of_death.jpg")).get_rect(), "text",
          text, "action", font.render("Начать сначала", False, WHITE, BEIGE)], "did_actions", "0", "max_actions", "1"]]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass