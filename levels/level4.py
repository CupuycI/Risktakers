import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path


background_img = pg.image.load(get_path("background_night_bandit_camp.jpg"))
music = [pg.mixer.Sound(get_path("Bonfire.mp3")), "bonfire"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Наконец-то меня довезли ', 'в лагерь бандитов. ', 'Через несколько минут', 'подходит бандит и спрашивает: ',
                 '"Какие ещё дела ты провернул?"']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0

level = "level4"
next_level = "level5"
original_cards = [[[pg.image.load(get_path("card_night_bandit.jpg")), pg.image.load(get_path("card_night_bandit.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_lie.jpg")), pg.image.load(get_path("card_lie.jpg")).get_rect(), "text",
                    ['-"В Техасе моё имя висело', 'на каждом столбе. ', 'Съезди и посмотри."', '-"Убедил"'], "action",
                    font.render("Солгать", False, WHITE, BEIGE), "effect", "distrust", "-1"],
                   [pg.image.load(get_path("card_rude.jpg")),
                    pg.image.load(get_path("card_rude.jpg")).get_rect(), "text",
                    ['-"Ты из любопытных что ли?"', '-"Ну и не говори"'], "action",
                    font.render("Нагрубить", False, WHITE, BEIGE), "effect", "distrust", "1"],
                   "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("card_playing_bandits.jpg")), pg.image.load(get_path("card_playing_bandits.jpg")).get_rect(), "text",
                  [], "action", font.render("Играть", False, WHITE, BEIGE), "effect", "money", 5, "random"],
                  [pg.image.load(get_path("card_go_out_from_playing_bandits.jpg")),
                   pg.image.load(get_path("card_go_out_from_playing_bandits.jpg")).get_rect(), "text",
                   ['Пойду спать'], "action", font.render("Уйти", False, WHITE, BEIGE), "effect_next_level"],
                   "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_bandit_leader_go_out.jpg")), pg.image.load(get_path("card_bandit_leader_go_out.jpg")).get_rect(), "text",
          ['Бандиты ложатся спать, ', 'но главарь куда-то уходит.']], "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("card_go_after_leader.jpg")), pg.image.load(get_path("card_go_after_leader.jpg")).get_rect(), "text",
  ['Спустя 2 минуты пути, ', 'главарь приветствует ковбоя', 'у реки.', 'Это же Том!',
   'Предатель говорит:', '"К вам должен внедриться ', 'агент шерифа, будь осторожен."',
   'После разговора главарь даёт', 'ему монеты и уходит.', 'Том пересчитывает деньги.'], "action",
  font.render("Проследить", False, WHITE, BEIGE), "effect", 'know_imposter', '1',
                   "effect_next_level", "change_next_level", "level_night_forest"],
                  [pg.image.load(get_path("card_sleep.jpg")),
                   pg.image.load(get_path("card_sleep.jpg")).get_rect(), "text",
                   ['За ночь меня никто', 'не потревожил.'], "action", font.render("Спать", False, WHITE, BEIGE),
                   "effect", "distrust", "1"], "did_actions", "0", "max_actions", "1"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    from random import choice
    if choice([0, 1]):
        cards[2][0][3] = ["Сегодня не мой день.", "(- 5 монет)"]
        cards[2][0][8] = -5
    else:
        cards[2][0][3] = ["Удача на моей стороне!", "(+ 5 монет)"]
        cards[2][0][8] = 5