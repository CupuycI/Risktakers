from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_blue_bandits_camp.jpg"))
music = [pg.mixer.Sound(get_path("Fight.mp3")), "fight"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Спустя несколько часов', "мы добрались и ", "окружили лагерь.", "На предложение сдаться",
                 "бандиты ответили выстрелами.", "Вдруг, я вижу", "главаря, забегающего в", "палатку."]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level6_3"
next_level = "level6_5"
original_cards = [[[pg.image.load(get_path("card_blue_bandit_leader.jpg")),
                   pg.image.load(get_path("card_blue_bandit_leader.jpg")).get_rect(), "text",
                   text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_follow_bandit_leader.jpg")),
                    pg.image.load(get_path("card_follow_bandit_leader.jpg")).get_rect(), "text",
                    ['В палатке меня ', "ждал бандит.", "Я пропустил удар, но", "успел выстрелить.",
                     "Палатка оказалась с",
                     "двумя входами.", "Главарь бежит в горный", "проход. Джеймс за ним.", "(- 1 сердце)"], "action",
                    font.render("Бежать за ним", False, WHITE, BEIGE), "effect",
                    "hearts", "-1"],
                   [pg.image.load(get_path("card_wait_bandit_leader.jpg")),
                    pg.image.load(get_path("card_wait_bandit_leader.jpg")).get_rect(), "text",
                    ["Из палатки выходит ", "бандит и падает", "после моего выстрела.", "Палатка оказалась с",
                     "двумя входами.",
                     "Главарь бежит в горный", "проход. Джеймс за ним."], "action",
                    font.render("Ждать", False, WHITE, BEIGE)], "did_actions", "0", "max_actions", "1"]]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass