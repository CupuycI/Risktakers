import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path

background_img = pg.image.load(get_path("background_town.jpg"))
music = [pg.mixer.Sound(get_path("town.mp3")), "town"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ["Наконец-то я добрался до города.", "Надо осмотреться.", "В трактире можно заказать", "еду и поиграть в карты.",
                 "Два ковбоя что-то бурно обсуждают."]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level2"
next_level = "level_horse_stable"
original_cards = [[[pg.image.load(get_path("came_to_town.jpg")), pg.image.load(get_path("came_to_town.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("eat_food.jpg")), pg.image.load(get_path("eat_food.jpg")).get_rect(), "text",
          ["Еда оказалась вкусной и сытной", "(+ 1 сердце, -5 монет)"], "action",
          font.render("Поесть в трактире за 5 монет", False, WHITE, BEIGE),
                   "effect", "hearts", "1", "effect2", "money", "-5"],
                  [pg.image.load(get_path("play_cards.jpg")), pg.image.load(get_path("play_cards.jpg")).get_rect(), "text",
          [], "action",
          font.render("Играть в карты. (Ставка: 5 монет)", False, WHITE, BEIGE), "effect", "money", 0, "random"],
          [pg.image.load(get_path("overhear_hunter.jpg")), pg.image.load(get_path("overhear_hunter.jpg")).get_rect(), "text",
          ["Охотник говорит, что видел банду!", "У него можно узнать их", "отличительные знаки."], "action",
          font.render("Подслушать разговор", False, WHITE, BEIGE), "effect_next_level"], "did_actions", "0", 'max_actions', '3'],

                  [[pg.image.load(get_path("ask_hunter_about_case.jpg")),
                    pg.image.load(get_path("ask_hunter_about_case.jpg")).get_rect(), "text",
                    ["Я спрашиваю, как выглядели ", "бандиты.", 'Охотник: "За информацию надо ', 'платить. Либо давай 5 монет, ', 'либо помоги в одном деле."'],
                    "action", font.render("Спросить", False, WHITE, BEIGE)],
                   [pg.image.load(get_path("go_out_from_hunter.jpg")),
                    pg.image.load(get_path("go_out_from_hunter.jpg")).get_rect(), "text",
                    ["Лучше пойду к шерифу."], "action", font.render("Уйти", False, WHITE, BEIGE), "effect_next_scene", "3"],
                   "did_actions", "0", "max_actions", "1"],

            [[pg.image.load(get_path("give_money_hunter.jpg")), pg.image.load(get_path("give_money_hunter.jpg")).get_rect(), "text",
          ["Охотник берёт монеты и говорит:", '"В синих шляпах и банданах."', "Это мне должно помочь.", "Пора идти к шерифу."],
              "action", font.render("Заплатить", False, WHITE, BEIGE), "effect", "money", "-5",
                   "effect2", "know_band", "1", "effect_next_scene", "2"],
                  [pg.image.load(get_path("ask_hunter_about_case.jpg")), pg.image.load(get_path("ask_hunter_about_case.jpg")).get_rect(), "text",
          ['Нужно будет проявить свою ', 'меткость с помощью мишени ', 'с конвертами, движущейся по дороге '],
                   "action", font.render("Спросить про дело", False, WHITE, BEIGE), "effect_next_level"],
                  [pg.image.load(get_path("go_out_from_hunter.jpg")), pg.image.load(get_path("go_out_from_hunter.jpg")).get_rect(), "text",
                   ["Лучше пойду к шерифу."], "action", font.render("Уйти", False, WHITE, BEIGE), "effect_next_scene", "2"],
             "did_actions", "0", "max_actions", "3"],

[[pg.image.load(get_path("answer_no.jpg")), pg.image.load(get_path("answer_no.jpg")).get_rect(), "text",
          ["Этот вариант мне не подходит."], "action", font.render("Не согласиться", False, WHITE, BEIGE),  "effect_back_scene", "-1", "1", "3"],
                  [pg.image.load(get_path("shoot.jpg")), pg.image.load(get_path("shoot.jpg")).get_rect(), "text",
          ['Дело сделано, охотник забирает ', 'какое-то письмо, и мы уходим. ', 'В городе он мне говорит: ', '"они были в синих шляпах и ', 'банданах"'],
                   "action", font.render("Согласиться", False, WHITE, BEIGE), "effect_next_level"],
                    "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("sheriff_in_his_cabinet.jpg")), pg.image.load(get_path("sheriff_in_his_cabinet.jpg")).get_rect(), "text",
  ["В комнате я вижу помощника ", "под именем Том и шерифа.", 'Выслушав мою историю, ',
   'Шериф говорит: "Внедрись в банду.',
   'Вот тебе листовка,', 'ты в розыске. Для легенды. Мой боец',
   'Сэм будет ждать тебя со 2-го ', 'по 5-й день в заброшенной мельнице. ', 'Попробуй внедриться через охотника.',
   'А, и возьми командировочные."', 'Нужно найти охотника.',
   '(+ 15 монет)'], "effect", "money", "15"], "did_actions", "0", "max_actions", "1"],

[[pg.image.load(get_path("main_street.jpg")), pg.image.load(get_path("main_street.jpg")).get_rect(), "text",
          ['Охотника здесь нет. ', 'Вот чёрт! ', 'Срезали один мешок монет!', '(- 5 монет)'], "action",
  font.render("Пойти на главную улицу", False, WHITE, BEIGE),  "effect", "money", "-5"],
                  [pg.image.load(get_path("saloon_card.jpg")), pg.image.load(get_path("saloon_card.jpg")).get_rect(), "text",
                   ['Здесь много подозрительных ', 'ковбоев, но охотника здесь нет. ',
                    'В меня врезается ковбой и говорит: ',
                    '"Эй, следи, куда идёшь!" ', 'Кажется, сейчас будет драка.', 'Ковбой замахивается кулаком.'], "action",
                   font.render("Пойти в салун", False, WHITE, BEIGE),
                   "effect_next_level", "change_next_level", "level_saloon"],
                  [pg.image.load(get_path("horse_stable_card.jpg")),
                   pg.image.load(get_path("horse_stable_card.jpg")).get_rect(), "text",
                   ['А вот и охотник!'], "action", font.render("Пойти в конюшню", False, WHITE, BEIGE),
                   "effect_next_level"], "did_actions", "0", "max_actions", "3"]
                  ]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    from random import choice
    if choice([0, 1]):
        cards[1][1][3] = ["Сегодня не мой день.", "(- 5 монет)"]
        cards[1][1][8] = -5
    else:
        cards[1][1][3] = ["Удача на моей стороне!", "(+ 5 монет)"]
        cards[1][1][8] = 5