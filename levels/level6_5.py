from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_gold_bearing.jpg"))
music = [pg.mixer.Sound(get_path("BossFight.mp3")), "bossfight"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Пробежав через проход, ', 'я вижу Джеймса Кольта,', "висящего на уступе ", "скалы и главаря бандитов,", "остановившегося при виде меня.",
                 "Чёрт! У меня", "закончились патроны."]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level6_5"
next_level = "level_final"
original_cards = [[[pg.image.load(get_path("card_level6_5.jpg")),
                   pg.image.load(get_path("card_level6_5.jpg")).get_rect(), "text",
                   text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_arrest.jpg")),
                    pg.image.load(get_path("card_arrest.jpg")).get_rect(), "text",
                    ['Я подхожу к главарю.', 'Начинается схватка.', 'Он резко достаёт клинок.'], "action",
                    font.render("Арестовать главаря", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("card_resque_sheriff.jpg")),
                    pg.image.load(get_path("card_resque_sheriff.jpg")).get_rect(), "text",
                    ["Главарь убегает, но я", "спасаю шерифа.", "Мы бежим за главарём."], "action",
                    font.render("Спасти шерифа", False, WHITE, BEIGE), "effect", "resque_sheriff", "1",
                    "do_create"],
                   "did_actions", "0", "max_actions", "1"],
                  []
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = 0
def create(game_data):
    if game_data["resque_sheriff"]:
        cards[2] = [[pg.image.load(get_path("card_blue_leader_swim_away.jpg")),
                   pg.image.load(get_path("card_blue_leader_swim_away.jpg")).get_rect(), "text",
                       ["Мы видим уплывающего", "на лодке главаря.", "Джеймс Кольт несколько раз ",
                        "стреляет, но не попадает.",
                        "Теперь его не догнать."]], "did_actions", "0", "max_actions", "1"]
        while len(cards) > 3:
            del cards[-1]
    else:
        while len(cards) > 3:
            del cards[-1]
        cards[2] = [[pg.image.load(get_path("card_jump_back.jpg")),
                   pg.image.load(get_path("card_jump_back.jpg")).get_rect(), "text",
                   ['Клинок не достаёт меня.', "Противник замахивается."], "action", font.render("Отпрыгнуть", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_lunge.jpg")),
                   pg.image.load(get_path("card_lunge.jpg")).get_rect(), "text",
                   ["Главарь отталкивает меня.", "Противник замахивается.", "(- 1 сердце)"], "action",
                   font.render("Сделать выпад", False, WHITE, BEIGE), "effect", "hearts",
                   "-1"],
                  [pg.image.load(get_path("card_block.jpg")),
                   pg.image.load(get_path("card_block.jpg")).get_rect(), "text",
                   ["Я успешно блокировал,", "но теперь ранен в руку.", "Противник замахивается.", "(- 1 сердце)"],
                   "action", font.render("Блокировать", False, WHITE, BEIGE), "effect", "hearts", "-1"],
                    "did_actions", "0", "max_actions", "1"]
        cards.append([[pg.image.load(get_path("card_jump_back.jpg")),
                   pg.image.load(get_path("card_jump_back.jpg")).get_rect(), "text",
                       ['Главарь кидает клинок', "и попадает в меня.", "Он начинает отходить назад", "и говорит:",
                        '"Ты из того поселения, да?', 'На месте которого теперь пепелище?"', " - и усмехается.",
                        "(- 2 сердца)"], "action", font.render("Отпрыгнуть", False, WHITE, BEIGE), "effect",
                       "hearts", "-2"],
                  [pg.image.load(get_path("card_hit2.jpg")),
                   pg.image.load(get_path("card_hit2.jpg")).get_rect(), "text",
                   ["Главарь роняет клинок.", "Он начинает отходить назад", "и говорит:",
                    '"Ты из того поселения, да?', 'На месте которого теперь пепелище?"', " - и усмехается."], "action",
                   font.render("Ударить", False, WHITE, BEIGE), "do_create"],
                  [pg.image.load(get_path("card_duck.jpg")),
                   pg.image.load(get_path("card_duck.jpg")).get_rect(), "text",
                   ["Это не смутило главаря,", "и он нанёс мне удар", "Он начинает отходить назад", "и говорит:",
                    '"Ты из того поселения, да?', 'На месте которого теперь пепелище?"', " - и усмехается.",
                    "(- 2 сердца)"], "action", font.render("Пригнуться", False, WHITE, BEIGE), "effect",
                   "hearts", "-2", "do_create"],
                      "did_actions", "0", "max_actions", "1"])
        if game_data["know_imposter"]:
            s = ['Противник кидает песок', "мне в глаза и набрасывается.", "Вдруг, звучит выстрел.",
                           "Главарь отходит от меня", "и сдаётся.", "Это Сэм.", "(- 1 сердце)"]
            n = "-1"
        else:
            hearts = game_data["hearts"]
            n = "-" + str(hearts)
            if hearts == 5:
                s = " сердец"
            elif hearts == 1:
                s = " сердце"
            else:
                s = " сердца"
            s = ['Противник кидает песок', "мне в глаза и набрасывается.",
                           "(- " + str(game_data["hearts"]) + s + ")"]
        cards.append([[pg.image.load(get_path("card_revolver.jpg")),
                   pg.image.load(get_path("card_revolver.jpg")).get_rect(), "text",
                   ["При виде револьвера", "главарь сдаётся."], "action", font.render("Достать револьвер", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_lunge2.jpg")),
                   pg.image.load(get_path("card_lunge2.jpg")).get_rect(), "text",
                   s, "action", font.render("Сделать выпад", False, WHITE, BEIGE), "effect", "hearts", n],
                      "did_actions", "0", "max_actions", "1"])
        cards.append([[pg.image.load(get_path("card_firestorm.jpg")),
                   pg.image.load(get_path("card_firestorm.jpg")).get_rect(), "text",
                   ["Я слышу людей, идущих", "сюда. Это бойцы Кольта.", "Я смотрю на край уступа,", "но не вижу Джеймса."]],
                      "did_actions", "0", "max_actions", "1"])
    global lst_i_mx
    lst_i_mx = len(cards)
