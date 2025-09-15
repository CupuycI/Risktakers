import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path


background_img = pg.image.load(get_path("background_horse_stable.jpg"))
music = [pg.mixer.Sound(get_path("horse_stable.mp3")), "horse_stable"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Охотник возится со своей лошадью.', 'Нужно добиться у него ', 'встречи с бандитами']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level_horse_stable"
next_level = "level_meet"
original_cards = [[[pg.image.load(get_path("card_hunter_with_horse.jpg")), pg.image.load(get_path("card_hunter_with_horse.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("talk1.jpg")), pg.image.load(get_path("talk1.jpg")).get_rect(), "text",
                    ['Охотник отвечает: "Какой из меня ', 'бандит? ', 'Это всего лишь слухи"'], "action",
                    font.render('"Прими меня в свою банду"', False, WHITE, BEIGE)],
                   [pg.image.load(get_path("talk2.jpg")), pg.image.load(get_path("talk2.jpg")).get_rect(), "text",
                    ['Охотник говорит: "Так иди в шахту, ', 'на охоту или на рыбалку. ', 'От меня ты что хочешь?"'],
                    "action", font.render('"Я хочу подзаработать"', False, WHITE, BEIGE)],
                   [pg.image.load(get_path("talk3.jpg")),
                    pg.image.load(get_path("talk3.jpg")).get_rect(), "text",
                    ['-"Я с напарниками выпытал у ', 'индейского вождя место, ', 'где их святилище. ',
                     'Но мы попали в засаду. ',
                     'Остался только я. ', 'Мне нужны новые бойцы.', 'В одиночку я вряд ли вынесу ', 'добычу оттуда"',
                     '-"Хм, помощь нужна? ', 'Ну хорошо, ', 'вечером будь в салуне."'], "action",
                    font.render("Рассказать выдуманную историю", False, WHITE, BEIGE),
                    "effect_next_level"], "did_actions", "0", "max_actions", "3"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    pass