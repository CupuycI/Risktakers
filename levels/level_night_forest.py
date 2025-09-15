from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path

background_img = pg.image.load(get_path("background_night_river.jpg"))
music = [pg.mixer.Sound(get_path("NightForest.wav")), "night_forest"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Помощник шерифа падает на землю.', 'И я ему подкладываю листовку.']
text = original_text[::]
text2 = ['Не мне его судить.']
did_actions = 0
max_actions = 1
lst_i = 0
level = "level_night_forest"
next_level = "level5"
original_cards = [[[pg.image.load(get_path("card_shoot_near_river.jpg")), pg.image.load(get_path("card_shoot_near_river.jpg")).get_rect(), "text",
          text, "action", font.render("Выстрелить", False, WHITE, BEIGE), "effect", "imposter_killed", "1"],
                  [pg.image.load(get_path("card_go_out_near_river.jpg")),
                   pg.image.load(get_path("card_go_out_near_river.jpg")).get_rect(), "text",
                   text2, "action", font.render("Уйти", False, WHITE, BEIGE), "effect",
                   "distrust", "1",
                   "effect_next_level", "change_next_level", "level5"], "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_wait.jpg")), pg.image.load(get_path("card_wait.jpg")).get_rect(), "text",
  ['Спустя 10 минут', 'приходят бандиты и главарь', 'Главарь спрашивает:', '-"Что здесь произошло?"',
   '-"Это помощник шерифа!', 'Он долгое время ', 'преследует меня.', 'До этого он втёрся в доверие',
   'моей прошлой банды ', 'и заложил её!"',
   'Все идут обратно в лагерь'], "action", font.render("Ждать", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_alarm.jpg")),
                   pg.image.load(get_path("card_alarm.jpg")).get_rect(), "text",
                   ['Я зову бандитов.', 'Спустя 10 минут', 'приходят бандиты и главарь', 'Главарь спрашивает:',
                   '-"Что здесь произошло?"',
                   '-"Это помощник шерифа!', 'Он долгое время ', 'преследует меня.', 'До этого он втёрся в доверие',
                   'моей прошлой банды ', 'и заложил её!"',
                   'Все идут обратно в лагерь'], "action", font.render("Поднять тревогу", False, WHITE, BEIGE), "effect",
                   "distrust", "-1"], "did_actions", "0", "max_actions", "1"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass
