from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_prairie.jpg"))
music = [pg.mixer.Sound(get_path("Duel.mp3")), "duel"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Вдалеке виднеется всадник.', 'Похоже, это тот самый ', 'матёрый бандит!', 'Он едет в заросли травы.', 'Нужно догнать его!']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level6"
next_level = "level6_3"
original_cards = [[[pg.image.load(get_path("card_experienced_bandit.jpg")),
                   pg.image.load(get_path("card_experienced_bandit.jpg")).get_rect(), "text",
                   text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_bypass.jpg")),
                    pg.image.load(get_path("card_bypass.jpg")).get_rect(), "text",
                    ['Я приближаюсь к бандиту.', "Вдруг, всадник сбавляет", "скорость."], "action",
                    font.render("Поехать в обход", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("card_thickets.jpg")),
                    pg.image.load(get_path("card_thickets.jpg")).get_rect(), "text",
                    ['Я приближаюсь к бандиту,', 'но он кидает горящую тряпку,', "и трава загорается.",
                     "Моя лошадь испугалась и",
                     "скинула меня, но я", "быстро залез обратно.", "Ещё есть шанс догнать его.",
                     "Вдруг, всадник сбавляет", "скорость.",
                     "(- 1 сердце)"], "action", font.render("Поехать за ним.", False, WHITE, BEIGE), "effect",
                    "hearts", "-1"], "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_ride_slow2.jpg")),
                   pg.image.load(get_path("card_ride_slow2.jpg")).get_rect(), "text",
                   ['Бандит резко достаёт револьвер,', 'но не попадает в меня.', "После этого шериф", "попадает в его лошадь.", "Теперь он не уйдёт."],
  "action", font.render("Замедлиться", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_ride_fast2.jpg")),
                   pg.image.load(get_path("card_ride_fast2.jpg")).get_rect(), "text",
                   ["Я приближаюсь, но", 'Бандит резко достаёт револьвер', "и стреляет в мою лошадь.",
                    "После этого шериф",
                    "попадает в его лошадь.", "Теперь он не уйдёт.", "(- 1 сердце)"], "action",
                   font.render("Ускориться", False, WHITE, BEIGE), "effect",
                   "hearts", "-1"], "did_actions", "0", "max_actions", "1"],

[[[]], "did_actions", "0", "max_actions", "1"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    if game_data["rifle"]:
        cards[1].insert(2, [pg.image.load(get_path("card_rifle.jpg")),
                      pg.image.load(get_path("card_rifle.jpg")).get_rect(), "text",
                      ['Я попадаю в его лошадь.', 'Теперь он не уйдёт.'], "action",
                      font.render("Выстрелить", False, WHITE, BEIGE), "effect_next_scene", "2"])
    if not game_data["know_imposter"]:
        cards[3] = [[pg.image.load(get_path("card_caught_bandit.jpg")),
                   pg.image.load(get_path("card_caught_bandit.jpg")).get_rect(), "text",
                     ['Шериф подъезжает к бандиту.', 'Вдруг, помощник шерифа', "стреляет, и бандит", "падает.",
                      "Помощник говорит, что ", "он тянулся за ", "револьвером."], "effect", "fox_caught", "1", "effect2",
                     "fox_killed", "1"],
                    "did_actions", "0", "max_actions", "1"]
    else:
        cards[3] = [[pg.image.load(get_path("card_caught_bandit.jpg")),
                   pg.image.load(get_path("card_caught_bandit.jpg")).get_rect(), "text",
                   ['Шериф подъезжает к бандиту', "и арестовывает его."], "effect", "fox_caught", "1"], "did_actions", "0", "max_actions", "1"]
    cards[3][0][3].append("Мы продолжаем путь.")