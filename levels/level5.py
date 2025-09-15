from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_merchant.jpg"))
music = [pg.mixer.Sound(get_path("Outlaw.mp3")), "Outlaw"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Утром банда отправляется закупать', 'снаряжение к торговцу. Многие ', 'берут патроны для револьвера.',
                 'Некоторые берут винтовки.', 'Один бандит взял динамит.', 'Подходит торговец и спрашивает:', '"Что будешь брать?"',
                 'Нужно что-то купить, ', 'иначе меня вычислят.', 'Патроны стоят 5 монет.', 'Винтовка стоит 15 монет.',
                 'Динамит стоит 10 монет.', 'Торговец говорит:', '"А, кстати, ваш лидер сказал ', 'продавать только по 1-му предмету ', 'на человека."']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level5"
next_level = "level5_4"
original_cards = [[[pg.image.load(get_path("card_merchant.jpg")), pg.image.load(get_path("card_merchant.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_cartridges.jpg")),
                    pg.image.load(get_path("card_cartridges.jpg")).get_rect(), "text",
                    ['Патроны мне явно пригодятся.', "(+ патроны для револьвера, -5 монет)"], "action",
                    font.render("Купить патроны", False, WHITE, BEIGE),
                    "effect", "cartridges", "1", "effect2", "money", "-5"],
                   [pg.image.load(get_path("card_rifle.jpg")),
                    pg.image.load(get_path("card_rifle.jpg")).get_rect(), "text",
                    ['Винтовка пригодится только', 'на средних и дальних дистанциях', "(+ винтовка, - 15 монет)"], "action",
                    font.render("Купить винтовку", False, WHITE, BEIGE),
                    "effect", "rifle", "1", "effect2", "money", "-15"],
                   [pg.image.load(get_path("card_dynamite.jpg")),
                    pg.image.load(get_path("card_dynamite.jpg")).get_rect(), "text",
                    ['Динамит - полезная вещь.', "(+ динамит, - 10 монет)"], "action",
                    font.render("Купить динамит", False, WHITE, BEIGE),
                    "effect", "dynamit", "1", "effect2", "money", "-10"],
                   "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_3_bandits.jpg")), pg.image.load(get_path("card_3_bandits.jpg")).get_rect(), "text",
          ['Ожидая остальных, три бандита ', 'тихо разговаривают между собой.', 'Это шанс узнать про банду', "поджигателей."]],
 "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_ask_bandits.jpg")), pg.image.load(get_path("card_ask_bandits.jpg")).get_rect(), "text",
          [], "action", font.render("Спросить про банды", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_overhear_bandits.jpg")),
                   pg.image.load(get_path("card_overhear_bandits.jpg")).get_rect(), "text",
                   ['Бандиты замечают меня и ', 'отталкивают.', '(- 1 сердце)'], "action",
                   font.render("Подслушать", False, WHITE, BEIGE), "effect", "hearts", "-1"],
                  [pg.image.load(get_path("card_go_out_slope.jpg")), pg.image.load(get_path("card_go_out_slope.jpg")).get_rect(), "text",
          ['Лучше я пойду.'], "action", font.render("Уйти", False, WHITE, BEIGE), "effect_next_level", "change_next_level", "level5_4"],
 "did_actions", "0", "max_actions", "3"],

                  [[pg.image.load(get_path("check_ashe.jpg")), pg.image.load(get_path("check_ashe.jpg")).get_rect(),
                    "text",
                    [], "action", font.render("Спросить про поджигателей", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("card_bribe_bandits.jpg")),
                    pg.image.load(get_path("card_bribe_bandits.jpg")).get_rect(), "text",
                    ['Бандиты отвечают: "Хорошо.', 'Это были Синие.','Они сейчас у истока ', 'реки Голдбэринг."', '(- 5 монет)'],
                    "action", font.render("Подкупить", False, WHITE, BEIGE), "effect", "money", "-5", "effect2",
                    "know_band_place", "1"], "did_actions", "0", "max_actions", "1"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    if game_data["distrust"] < 3:
        cards[3][0][3] = ['Бандиты перечисляют банды:', '"Чёрные псы, Барсы, Тени', 'Красные шарфы, Лесники..."']
        cards[3][0].append("effect_next_scene")
        cards[3][0].append("1")
    else:
        cards[3][0][3] = ['Бандиты говорят, что не знают']
        cards[3][0].append("effect_next_level")
        cards[3][0].append("change_next_level")
        cards[3][0].append("level5_4")
    if game_data["distrust"] < 2:
        cards[4][0][3] = ['Бандиты отвечают: "Это Синие.', 'Они сейчас у истока ', 'реки Голдбэринг."']
        cards[4][0].append("effect")
        cards[4][0].append("know_place_band")
        cards[4][0].append("1")
    else:
        cards[4][0][3] = ['Бандиты говорят, что не знают.']
    if game_data["know_band"]:
        cards[4].insert(2, [pg.image.load(get_path("bandit_at_ashe.jpg")),
                   pg.image.load(get_path("bandit_at_ashe.jpg")).get_rect(), "text",
                   ['Бандиты отвечают: "Это Синие.', 'Они сейчас у истока ', 'реки Голдбэринг."'],
                      "action", font.render("Спросить про синих бандитов", False, WHITE, BEIGE), "effect", "know_place_band", "1"])
