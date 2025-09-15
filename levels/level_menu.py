import pygame as pg
from functions import get_path

background_img = pg.image.load(get_path("menu_background_img.jpg"))
music = [pg.mixer.Sound(get_path("Ennio_Morricone_-_The_Good_The_Bad_And_The_Ugly_OST_KHoroshijj_plokhojj_zlojj_69334241.mp3")), "menu"]
font3 = pg.font.SysFont("arial", 60, False,  False)
buttons = [[font3.render("Новая игра", False, (255, 255, 255), None),
            font3.render("Новая игра", False, (255, 255, 255), None).get_rect(), "new_game"],
           [font3.render("Продолжить", False, (255, 255, 255), None),
            font3.render("Продолжить", False, (255, 255, 255), None).get_rect(), "current_level"],
           [font3.render("Настройки", False, (255, 255, 255), None),
            font3.render("Настройки", False, (255, 255, 255), None).get_rect(), "settings"],
           [font3.render("Выйти", False, (255, 255, 255), None),
            font3.render("Выйти", False, (255, 255, 255), None).get_rect(), "quit"]]
