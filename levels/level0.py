import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path

background_img = pg.image.load(get_path("background_hunter_field.jpg"))
music = [pg.mixer.Sound(get_path("Bird_Sounds_-_Bird_Sound_68938279.mp3")), "birds"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ["Я отправляюсь на охоту, полон", "оптимизма и готовности встретиться", "с дикой природой"]
text = original_text[::]
def create(game_data):
    pass
lst_i = 0
did_actions = 0
max_actions = 0
level = "level0"
next_level = "level1"
original_cards = [[[pg.image.load(get_path("riding_on_hunt.jpg")),
                    pg.image.load(get_path("riding_on_hunt.jpg")).get_rect(),
                    "text", ["Я отправляюсь на охоту, полон", "оптимизма и готовности встретиться", "с дикой природой"]
                    ], "did_actions", "0", "max_actions", "1"],
[[pg.image.load(get_path("enjoy_scenary.jpg")),
  pg.image.load(get_path("enjoy_scenary.jpg")).get_rect(), "text",
          ["Пейзажи восхитительны, но мне пора ", "возвращаться"], "action",
          font.render("Насладиться пейзажами", False, WHITE, BEIGE)],
         [pg.image.load(get_path("hunt.jpg")),
          pg.image.load(get_path("hunt.jpg")).get_rect(), "text",
          ["Стрела попадает прямо в цель.", "Побыв некоторое время на костре,", "добыча оказывается съедобной и",
           "вкусной.",
           "Пора возвращаться.", "(+ 1 сердце)"], "action",
          font.render("Охотиться", False, WHITE, BEIGE), "effect", "hearts", "1"
          ], "did_actions", "0", "max_actions", "1"],
                  [[pg.image.load(get_path("long_road.jpg")),
                    pg.image.load(get_path("enjoy_scenary.jpg")).get_rect(),
                    "text",
                    ["Места здесь прекрасные...", "Поселение будет видно за поворотом"], "action",
                    font.render("Вернуться длинной дорогой", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("short_road.jpg")), pg.image.load(get_path("short_road.jpg")).get_rect(), "text",
                    ["Места здесь обычные, зато скоро", "должно показаться поселение"], "action",
                    font.render("Вернуться короткой дорогой", False, WHITE, BEIGE), "effect", "know_band", "1"], "did_actions", "0", "max_actions", "1"]
                  ]
cards = [[j[::] for j in i[::]] for i in original_cards]
lst_i_mx = len(cards)