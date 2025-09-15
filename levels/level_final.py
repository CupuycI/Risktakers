from colors import WHITE, BEIGE
import pygame as pg
from functions import get_path

size = 45
background_img = pg.image.load(get_path("background_final.jpg"))
music = ['', "final"]
font = pg.font.SysFont("arial", size, False, False)
original_text = [""]
text = original_text[::]
did_actions = 0
max_actions = 1
lst_i = 0
level = "level_final"
next_level = "level_menu"
original_cards = [[[pg.image.load(get_path("card_final.jpg")),
                   pg.image.load(get_path("card_final.jpg")).get_rect(), "text",
                   text, "final"], "did_actions", "0", "max_actions", "1"]]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    s = ''
    score = 0
    if game_data["scorpions_caught"]:
        s += 'Банда "Скорпионы", терроризирующая караваны, арестована. Путники, купцы и дилижансы благодарны. '
        score += 1
    else:
        s += 'Банда "Скорпионы", терроризирующая караваны, ушла в другой штат. '
    if game_data["fox_killed"]:
        s += '"Хитрый Лис", выбравшийся из многих передряг, погиб. '
    elif game_data["fox_caught"]:
        s += '"Хитрый Лис", выбравшийся из многих передряг, арестован. '
        score += 1
    else:
        s += '"Хитрый Лис", выбравшийся из многих передряг, скрылся. '
        score -= 1
    if game_data["know_imposter"]:
        if game_data["imposter_killed"]:
            s += "Том, предавший Кольта, погиб. "
            score += 1
        else:
            from random import choice
            if game_data["imposter_caught"] == 2:
                game_data["imposter_caught"] += choice([0, 1])
            if game_data["imposter_caught"] == 3:
                s += "Том, предавший Кольта, арестован. "
                score += 1
            else:
                s += "Том, предавший Кольта, сбежал."
    elif game_data["know_place_band"]:
        s += "Том оказался предателем и сбежал. От его рук погиб Сэм. "
        score -= 1
    else:
        s += "Том оказался предателем и сбежал."

    if game_data["know_band"]:
        if game_data["know_place_band"]:
            s += 'Банда "Синие", держащая в страхе многих, арестована. Ковбои ликуют. '
            score += 1
            if not game_data["resque_sheriff"]:
                s += '"Огненный Шторм", известный своей тягой к холодному оружию и огню, арестован. '
                s += 'Шериф Джеймс Кольт пропал без вести. '
                score -= 1
            else:
                s += '"Огненный Шторм", известный своей тягой к холодному оружию и огню, сбежал.'
        else:
            s += 'Банда "Синие", держащая в страхе многих, ушла в другой штат. '
            s += '"Огненный Шторм", известный своей тягой к холодному оружию и огню, сбежал.'
    if score >= 2:
        music[0] = pg.mixer.Sound(get_path("HappyEnd.mp3"))
    elif score >= 0:
        music[0] = pg.mixer.Sound(get_path("NeutralEnd.mp3"))
    else:
        music[0] = pg.mixer.Sound(get_path("BadEnd.mp3"))

    lst = []
    s = s.split()
    size2 = 2416
    while True:
        if len(s) == 0:
            break
        s2 = ""
        for i in s:
            if len(s2 + i) * size <= size2:
                s2 += ' ' + i
            else:
                break

        s = " ".join(s)[len(s2):].split()
        lst.append(s2)
    if len(lst) < 10:
        for i in range(10 - len(lst) // 2):
            lst.insert(0, '')
    cards[0][0][3] = lst
