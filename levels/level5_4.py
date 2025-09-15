from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_bandit_camp2.jpg"))
music = [pg.mixer.Sound(get_path("NightForest.wav")), "night_forest"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Банда останавливается на ночь.', 'Главарь объявляет, что за ущельем', 'их ждёт матёрый бандит,',
                 '"Хитрый лис" Джон,',
                 'друг того, за кого я себя выдаю.', "Нужно сообщить об этом шерифу."]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level5_4"
next_level = "level5_7"
original_cards = [[[pg.image.load(get_path("card_bandit_leader2.jpg")), pg.image.load(get_path("card_bandit_leader2.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_windmill.jpg")), pg.image.load(get_path("card_windmill.jpg")).get_rect(),
                    "text",
                    ['Зайдя в мельницу, я вижу Сэма.', 'Выслушав меня, он говорит:', '"Дальше ущелья банда не пройдёт.',
                     'Тебе пора идти, а то ', 'бандиты что-то заподозрят.', 'До встречи."']], "did_actions", "0", "max_actions",
                   "1"],

[[pg.image.load(get_path("card_night_bandit2.jpg")), pg.image.load(get_path("card_night_bandit2.jpg")).get_rect(), "text",
          ['В лагере меня встречает главарь,', 'но ничего не говорит.'], "effect", "distrust", "1"], "did_actions", "0",
 "max_actions", "1"]]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass