import pygame as pg
from colors import WHITE, BEIGE
from functions import get_path


background_img = pg.image.load(get_path("background_ashes.jpg"))
music = [pg.mixer.Sound(get_path("ashes.mp3")), "ashes"]
font = pg.font.SysFont("arial", 25, False, False)
original_text = ["На месте города теперь пепелище.", "Я должен выяснить, кто это сделал.", "В городке неподалёку есть шериф,",
                 "Джеймс Кольт. Отправлюсь туда."]
text = original_text[::]
lst_i = 0
did_actions = 0
max_actions = 1
level = "level1"
next_level = "level2"
original_cards = [[[pg.image.load(get_path("ashes.jpg")), pg.image.load(get_path("ashes.jpg")).get_rect(), "text",
          text], "did_actions", "0", "max_actions", "1"],

                  [[pg.image.load(get_path("check_ashe.jpg")), pg.image.load(get_path("check_ashe.jpg")).get_rect(), "text",
                    ["Спустя 10 минут надежда ", "что-то найти угасает.", "Так, что это тут?",
                     "Мешок монет! Это мне пригодится.",
                     "Пора в путь", "(+ 10 монет)"], "action",
          font.render("Осмотреть пепелище", False, WHITE, BEIGE), "effect", "money", "10"],
         [pg.image.load(get_path("road_from_ashe.jpg")), pg.image.load(get_path("road_from_ashe.jpg")).get_rect(), "text",
          ["У меня нет желания дальше здесь", "оставаться, пора в путь."], "action",
          font.render("Отправиться в путь", False, WHITE, BEIGE), "effect", "next_level", "1"], "did_actions", "0", "max_actions", "1"]]
cards = [i[::] for i in original_cards]
lst_i_mx = len(cards)
def create(game_data):
    if game_data["know_band"]:
        cards[0][0][3] = ["На месте города теперь пепелище.", "Я должен выяснить, кто это сделал.", "В городке неподалёку есть шериф,",
                 "Джеймс Кольт. Отправлюсь туда.", "Кажется, там кто-то есть.", "Это бандит!"]
    else:
        cards[0][0][3] = ["На месте города теперь пепелище.", "Я должен выяснить, кто это сделал.", "В городке неподалёку есть шериф,",
                 "Джеймс Кольт. Отправлюсь туда."]
    if game_data["know_band"]:

        cards[1].insert(2, ([pg.image.load(get_path("bandit_at_ashe.jpg")), pg.image.load(get_path("bandit_at_ashe.jpg")).get_rect(), "text",
                      ["Я всё ближе и ближе к бандиту.", "Вдруг, бандит достаёт револьвер", "и стреляет в мою лошадь.", "Падение оказалось не из приятных.",
                       "Бандита мне теперь не догнать,", "а в город придётся добираться ", "пешком.", "(- 1 сердце)"], "action",
                      font.render("Погнаться за бандитом", False, WHITE, BEIGE), "effect", "hearts", "-1"]))