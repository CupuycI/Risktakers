import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path


background_img = pg.image.load(get_path("background_saloon.jpg"))
music = [pg.mixer.Sound(get_path("NoCompromiseSolution.mp3")), "saloon"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Зайдя в салун, я увидел 3-х ковбоев,', 'сидящих за столом и смотрящих ', 'на меня.', 'Похоже, это с ними у меня встреча.',
                 'Я сажусь за стол, и они ', 'меня приветствуют.', 'Один бандит говорит: ', '"Мы из банды "Скорпионы".', 'Обсудим условия, а потом ', 'поедем в лагерь.',
                 'Сколько добычи достанется нам?"']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level_meet"
next_level = "level4"
original_cards = [[[pg.image.load(get_path("meet_at_saloon.jpg")), pg.image.load(get_path("meet_at_saloon.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("meet_at_saloon.jpg")), pg.image.load(get_path("meet_at_saloon.jpg")).get_rect(), "text",
          ['Бандит говорит: ', '"Мы не согласимся на меньшее 50%."'], "action", font.render('30%', False, WHITE, BEIGE)],
                  [pg.image.load(get_path("meet_at_saloon.jpg")), pg.image.load(get_path("meet_at_saloon.jpg")).get_rect(), "text",
          ['Бандит говорит: "Мы согласны."'], "action", font.render('50%', False, WHITE, BEIGE), "effect_next_level"],
                  [pg.image.load(get_path("meet_at_saloon.jpg")),
                   pg.image.load(get_path("meet_at_saloon.jpg")).get_rect(), "text",
                   ['Бандит говорит: ', '"Так много? Ладно, мы согласны."'], "action",
                   font.render("70%", False, WHITE, BEIGE), "effect", "distrust", "1", "effect_next_level"],
 "did_actions", "0", "max_actions", "2"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass