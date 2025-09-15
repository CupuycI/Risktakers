from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path


background_img = pg.image.load(get_path("background_gorge.jpg"))
music = [pg.mixer.Sound(get_path("Prairie.mp3")), "Prairie"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ['Связанных бандитов отправляют', 'с конвоем в город. Шериф подходит', 'и говорит: "Молодец!"']
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level5_8"
next_level = "level6"
original_cards = [[[]]]
cards = [i[::] for i in original_cards]
lst_i_mx = 0
def create(game_data):
    if game_data["scorpions_caught"]:
        cards[0] = [[pg.image.load(get_path("card_exit_gorge.jpg")),
                   pg.image.load(get_path("card_exit_gorge.jpg")).get_rect(), "text",
                   text], "did_actions", "0", "max_actions", "1"]
    else:
        cards[0] = [[pg.image.load(get_path("card_exit_gorge.jpg")),
                     pg.image.load(get_path("card_exit_gorge.jpg")).get_rect(), "text",
                     ['Шериф приветствует меня ', 'и говорит: "Эта банда ушла, ', 'зато вторая неподалёку."']],
                    "did_actions", "0", "max_actions", "1"]
    if not game_data["imposter_killed"]:
        if game_data["know_imposter"]:
            for i in ['Вдруг, к шерифу подходит ', 'его помощник.', 'Я раскрываю предателя.', 'Он резко достаёт револьвер, ',
                        'но шериф выбивает пистолет', ' у него из рук.', 'Помощника арестовывают.', 'Шериф узнаёт у него', 'местоположение второй банды.',
                        'Шериф говорит, что нужно ', 'отправить его в город,', 'но бойцы нужны для ', 'ареста поджигателей.']:
                cards[0][0][3].append(i)
            cards[0][0].append("effect2")
            cards[0][0].append("know_place_band")
            cards[0][0].append("1")
            cards.append([[pg.image.load(get_path("card_imposter_gorge.jpg")),
                pg.image.load(get_path("card_imposter_gorge.jpg")).get_rect(), "text",
                ['Сначала нужно забрать', 'у него вещи, которые', 'могут помочь при побеге.']], "did_actions", "0",
                            "max_actions", "1"])

            cards.append([[pg.image.load(get_path("card_small_stone.jpg")),
                pg.image.load(get_path("card_small_stone.jpg")).get_rect(), "text",
                ['Камень конфискован.'], "action", font.render("Камень", False, WHITE, BEIGE), "effect",
                "imposter_caught", "-1"],
                [pg.image.load(get_path("card_pepper.jpg")),
                pg.image.load(get_path("card_pepper.jpg")).get_rect(), "text",
                ['Я забираю перец.'], "action", font.render("Перец", False, WHITE, BEIGE), "effect",
                "imposter_caught", "1"],
                [pg.image.load(get_path("card_coin.jpg")),
                pg.image.load(get_path("card_coin.jpg")).get_rect(), "text",
                ['Я хочу забрать монету,', 'но предатель выкидывает её.'], "action",
                font.render("Монета", False, WHITE, BEIGE), "effect",
                "imposter_caught", "-1"], "did_actions", "0", "max_actions", "1"])

            cards.append([[pg.image.load(get_path("card_flask.jpg")),
                pg.image.load(get_path("card_flask.jpg")).get_rect(), "text",
                ['Я тянусь к фляге, но', "предатель отталкивает меня.", 'Шериф: "Пусть оставит себе."'], "action",
                            font.render("Фляга", False, WHITE, BEIGE), "effect",
                "imposter_caught", "-1"],
                [pg.image.load(get_path("card_whistle.jpg")),
                pg.image.load(get_path("card_whistle.jpg")).get_rect(), "text",
                ['Я забираю свистульку.'], "action", font.render("Свистулька", False, WHITE, BEIGE), "effect",
                "imposter_caught", "1"],
                [pg.image.load(get_path("card_cup.jpg")),
                pg.image.load(get_path("card_cup.jpg")).get_rect(), "text",
                ['Я забираю кружку.'], "action", font.render("Кружка", False, WHITE, BEIGE), "effect",
                "imposter_caught", "-1"], "did_actions", "0", "max_actions", "1"])

            cards.append([[pg.image.load(get_path("card_rope.jpg")),
                pg.image.load(get_path("card_rope.jpg")).get_rect(), "text",
                ['Боец привязывает преступника ', 'к сосне.'], "action",
                            font.render("Оставить связанным", False, WHITE, BEIGE), "effect",
                "imposter_caught", "-1"],
                [pg.image.load(get_path("card_one_cowboy.jpg")),
                pg.image.load(get_path("card_one_cowboy.jpg")).get_rect(), "text",
                ['Боец увозит преступника.'], "action",
                font.render("Отправить с одним бойцом", False, WHITE, BEIGE), "effect",
                "imposter_caught", "0"],
                [pg.image.load(get_path("card_three_cowboys.jpg")),
                pg.image.load(get_path("card_three_cowboys.jpg")).get_rect(), "text",
                ['Бойцы увозят преступника.'], "action",
                font.render("Отправить с тремя бойцами", False, WHITE, BEIGE), "effect",
                "imposter_caught", "1"], "did_actions", "0", "max_actions", "1"])
            from random import choice
            cards[4][1][8] = str(choice([0, 1]))
        else:
            for i in ['Вдруг, к шерифу подходит ', 'его помощник', 'и приветствует меня.']:
                cards[0][0][3].append(i)
    if game_data["know_place_band"]:
        cards.append([[pg.image.load(get_path("card_sheriff_gorge.jpg")),
                pg.image.load(get_path("card_sheriff_gorge.jpg")).get_rect(), "text",
                ['Шериф говорит: "Время брать', 'вторую банду."', 'Мы отправляемся к истоку', 'реки Голдбэринг.']],
                        "did_actions", "0", "max_actions", "1"])
    else:
        cards.append([[pg.image.load(get_path("card_sheriff_gorge.jpg")),
                pg.image.load(get_path("card_sheriff_gorge.jpg")).get_rect(), "text",
                ['Мы не знаем, где искать', 'вторую банду.'], "effect_next_level", "change_next_level", "level_final"],
                        "did_actions", "0", "max-actions", "1"])

    global lst_i_mx
    lst_i_mx = len(cards)
