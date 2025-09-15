from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path

background_img = pg.image.load(get_path("background_merchant.jpg"))
music = [pg.mixer.Sound(get_path("Outlaw.mp3")), "Outlaw"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['']
text = original_text[::]
text2 = ['Бандиты замечают меня и ', 'отталкивают.', '(- 1 сердце)']
text3 = ['Лучше я пойду.']
did_actions = 0
max_actions = 1
lst_i = 0
level = "level5_7"
next_level = "level5_8"
original_cards = [[[pg.image.load(get_path("card_ask_bandits.jpg")), pg.image.load(get_path("card_ask_bandits.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"], [], []]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    global background_img
    if game_data["distrust"] >= 3:
        background_img = pg.image.load(get_path("background_prairie.jpg"))
        cards[0] = [[pg.image.load(get_path("card_escape.jpg")), pg.image.load(get_path("card_escape.jpg")).get_rect(), "text",
          ['Разбойники вычислили меня!', 'Я быстро прыгаю на лошадь.']], "did_actions", "0", "max_actions", "1"]
        cards[1] = [[pg.image.load(get_path("card_ride_fast.jpg")),
                   pg.image.load(get_path("card_ride_fast.jpg")).get_rect(), "text",
                   ['Я отрываюсь от бандитов.', 'Но впереди река, справа мост ', 'через неё, а слева лес.'], "action",
                     font.render("Скакать галопом", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_ride_slow.jpg")),
                   pg.image.load(get_path("card_ride_slow.jpg")).get_rect(), "text",
                   ['Один бандит попадает в меня из ', 'револьвера.', 'Впереди река, справа мост ',
                    'через неё, а слева лес.',
                    "(- 1 сердце)"], "action", font.render("Скакать рысью", False, WHITE, BEIGE), "effect",
                   "hearts", "-1"], "did_actions", "0", "max_actions", "1"]
        cards[2] = [[pg.image.load(get_path("card_river2.jpg")),
                   pg.image.load(get_path("card_river2.jpg")).get_rect(), "text",
                   ['Лошадь медлит и падает после ', 'выстрела бандита, скинув меня', 'Бандиты прекращают преследование.',"(- 1 сердце)"],
                     "action", font.render("Скакать через реку", False, WHITE, BEIGE), "effect",
                   "hearts", "-1"],
                  [pg.image.load(get_path("card_bridge.jpg")),
                   pg.image.load(get_path("card_bridge.jpg")).get_rect(), "text",
                   ['Я почти проехал через мост, ', 'но лошадь падает после ', 'выстрела бандита, скинув меня.',
                    'Бандиты прекращают преследование.',
                    "(- 1 сердце)"], "action", font.render("Скакать по мосту", False, WHITE, BEIGE), "effect",
                   "hearts", "-1"],
                  [pg.image.load(get_path("card_forest.jpg")),
                   pg.image.load(get_path("card_forest.jpg")).get_rect(), "text",
                   ['В лесу я быстро скрылся от погони', "и приехал к шерифу."], "action",
                   font.render("Скакать в лес", False, WHITE, BEIGE)],
                    "did_actions", "0", "max_actions", "1"]
    elif game_data["distrust"] == 2:
        background_img = pg.image.load("background_forest.jpg")
        cards[0] = [
            [pg.image.load(get_path("card_change_route.jpg")), pg.image.load(get_path("card_change_route.jpg")).get_rect(), "text",
             ['Главарь поменял маршрут. ', 'Нужно переубедить его!']], "did_actions", "0", "max_actions", "1"]
        cards[1] = [[pg.image.load(get_path("card_explain.jpg")),
                   pg.image.load(get_path("card_explain.jpg")).get_rect(), "text",
                     ['-"Через ущелье путь короче, значит,', 'нужно меньше провизии и выше',
                      'шанс не найти святилище пустым."',
                      'Главарь: "Ладно, убедил."'], "action", font.render('"Через ущелье путь короче"', False, WHITE, BEIGE),
                   "effect", "distrust", "-7", "effect_next_scene", "-1", "do_create"],
                  [pg.image.load(get_path("card_rude_2.jpg")),
                   pg.image.load(get_path("card_rude_2.jpg")).get_rect(), "text",
                   ['За грубость я получаю удар.', 'Банда идёт в обход.', 'Нужно незаметно уехать.',
                    "(- 1 сердце)"], "action", font.render("Нагрубить", False, WHITE, BEIGE), "effect",
                   "hearts", "-1"],
                  [pg.image.load(get_path("card_agree.jpg")),
                   pg.image.load(get_path("card_agree.jpg")).get_rect(), "text",
                   ['Банда идёт в обход.', 'Нужно незаметно уехать.'], "action",
                   font.render("Согласиться", False, WHITE, BEIGE)],
                    "did_actions", "0", "max_actions", "1"]
        cards[2] = [[pg.image.load(get_path("card_fast_turn.jpg")),
                   pg.image.load(get_path("card_fast_turn.jpg")).get_rect(), "text",
                   ['Когда бандиты понимают, ', 'что произошло, меня уже не догнать.', 'Отправлюсь к шерифу.'],
                     "action", font.render('Резко свернуть в лес', False, WHITE, BEIGE),
                   "effect_next_level"],
                  [pg.image.load(get_path("card_fall_behind.jpg")),
                   pg.image.load(get_path("card_fall_behind.jpg")).get_rect(), "text",
                   ['Бандиты замечают и говорят не спать.'], "action", font.render("Отстать", False, WHITE, BEIGE)],
                  [pg.image.load(get_path("card_slow_turn.jpg")),
                   pg.image.load(get_path("card_slow_turn.jpg")).get_rect(), "text",
                   ['Бандиты замечают и говорят ', 'не отставать.'], "action",
                   font.render("Медленно свернуть в лес", False, WHITE, BEIGE)], "did_actions", "0",
                    "max_actions", "3"]
    else:

        background_img = pg.image.load(get_path("background_gorge.jpg"))
        cards[0] = [
            [pg.image.load(get_path("card_put_tail.jpg")),
             pg.image.load(get_path("card_put_tail.jpg")).get_rect(), "text",
             ['Главарь установил за мной слежку.']], "did_actions", "0", "max_actions", "1"]
        cards[1] = [[pg.image.load(get_path("card_band_enter_gorge.jpg")),
                    pg.image.load(get_path("card_band_enter_gorge.jpg")).get_rect(), "text",
                    ['Банда заезжает в ущелье.', 'Вдруг, на краю ущелья виднеется ', 'шериф. Он показывает, что мне ', 'нужно вырваться вперёд банды.']],
                   "did_actions", "0", "max_actions", "1"]
        cards[2] = [[pg.image.load(get_path("card_stone_gorge.jpg")),
                   pg.image.load(get_path("card_stone_gorge.jpg")).get_rect(), "text",
                     ['Я спрыгиваю и прячусь за камнем.', "После этого шериф и его бойцы",
                      "делают предупредительные ", "выстрелы,", "и банда сдаётся."], "action",
                     font.render("Спрятаться", False, WHITE, BEIGE), "effect", "scorpions_caught", "1"],
                  [pg.image.load(get_path("card_run_gorge.jpg")),
                   pg.image.load(get_path("card_run_gorge.jpg")).get_rect(), "text",
                   ['Я скачу вперёд со всей скорости,', "но один бандит стреляет в ", "мою лошадь,",
                    "и я падаю вместе с ней.",
                    "После этого шериф и его бойцы", "делают предупредительные ", "выстрелы,", "и банда сдаётся.",
                    "(- 1 сердце)"], "action", font.render("Быстро ехать вперёд", False, WHITE, BEIGE), "effect",
                   "hearts", "-1", "effect2", "scorpions_caught", "1"], "did_actions", "0", "max_actions", "1"]
        if game_data["dynamit"]:
            cards[2].insert(2, [pg.image.load(get_path("card_explosion_gorge.jpg")),
                          pg.image.load(get_path("card_explosion_gorge.jpg")).get_rect(), "text",
                          ["Теперь меня и банду разделяет ", "завал.", "После этого шериф и его бойцы",
                           "делают предупредительные ", "выстрелы,", "и банда сдаётся."],
                          "action", font.render("Кинуть динамит позади себя", False, WHITE, BEIGE), "effect", "scorpions_caught", "1"])
