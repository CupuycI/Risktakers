import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path


background_img = pg.image.load(get_path("background_saloon.jpg"))
music = [pg.mixer.Sound(get_path("Saloon.mp3")), "saloon"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Я быстро уворачиваюсь,', 'и ковбой промазывает.', 'Противник делает рывок.']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
text2 = ['Противник оказался быстрее', 'Противник делает рывок.', '(- 1 сердце)']
text3 = ['Ковбой отлетает в стол,', 'но быстро возвращается к схватке', 'Противник делает рывок.']
level = "level_saloon"
next_level = "level2"
original_cards = [[[pg.image.load(get_path("dodge.jpg")), pg.image.load(get_path("dodge.jpg")).get_rect(), "text",
          text, "action", font.render("Увернуться", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("hit.jpg")), pg.image.load(get_path("hit.jpg")).get_rect(), "text",
          text2, "action", font.render("Ударить", False, WHITE, BEIGE),
                   "effect", "hearts", "-1"],
                  [pg.image.load(get_path("push_by_leg.jpg")),
                   pg.image.load(get_path("push_by_leg.jpg")).get_rect(), "text",
                   text3, "action", font.render("Толкнуть ногой", False, WHITE, BEIGE)], "did_actions", "0",
                   "max_actions", "1"
                  ],

                  [[pg.image.load(get_path("dodge.jpg")), pg.image.load(get_path("dodge.jpg")).get_rect(), "text",
                    ['Ковбой врезается в стол.', 'Он спотыкается и ', 'падает на пол.', 'Поединок завершается под ', 'аплодисменты'],
                    "action", font.render("Увернуться", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("hit.jpg")), pg.image.load(get_path("hit.jpg")).get_rect(), "text",
                    ['Противник оказался быстрее', 'Он спотыкается и ', 'падает на пол.', 'Поединок завершается под ', 'аплодисменты', '(- 1 сердце)'],
                    "action", font.render("Ударить", False, WHITE, BEIGE),
                    "effect", "hearts", "-1"], "did_actions", "0", "max_actions", "1", "scene", "6"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass