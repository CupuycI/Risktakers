import pygame as pg
from functions import get_path

background_img = pg.image.load(get_path("settings.jpg"))
music = [pg.mixer.Sound(get_path("Ennio_Morricone_-_The_Good_The_Bad_And_The_Ugly_OST_KHoroshijj_plokhojj_zlojj_69334241.mp3")), "menu"]
font3 = pg.font.SysFont("arial", 60, False,  False)
button_exit = [font3.render("Вернуться", False, (255, 255, 255), None),
                font3.render("Вернуться", False, (255, 255, 255), None).get_rect()]