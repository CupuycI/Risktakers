import pygame as pg
from colors import *
from functions import *
from list_of_levels import list_of_levels

pg.init()
pg.mixer.init()


config = load_stats("configuration.py", create_configuration, "Risktakers")
game_data = create_game_data()
SIZE = (1920, 1096)
level = my_import("level_menu")

font = pg.font.SysFont("arial", 25, False, False)

screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

background_img_rect = pg.Rect(0, 0, SIZE[0], SIZE[1])

menu = 1
death = 0
esc_pressed = 0
run = 1
lst_i = 0
mx = 0
did = 0
scene = 0
do_create = 0
settings_menu = 0
enter = 0
s2 = ""
music = level.music
s = config["volume"]
while run:
    if not pg.mixer.get_busy():
        music[0].set_volume(int(s) / 100)
        music[0].play()
    for event in pg.event.get():
        if enter and settings_menu:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_IBEAM)
            if event.type == pg.KEYDOWN:
                if event.unicode.isdigit():
                    s += event.unicode
                    if int(s) > 100:
                        s = "100"
                elif event.key == pg.K_BACKSPACE:
                    s = s[:-1]
                elif event.key == 13:
                    enter = 0
                    music[0].set_volume(int(s) / 100)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)


        if event.type == pg.QUIT:
            run = 0
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if menu:
                button = 0
                for i in level.buttons:
                    if i[1].collidepoint(event.pos):
                        button = i[::]
                        break
                if button:
                    if button[2] == "new_game":

                        game_reset(list_of_levels)
                        game_data = create_game_data()
                        game_data2 = game_data.copy()
                        music[0].stop()
                        level = my_import(game_data["level"])
                        level.did_actions = 0
                        level.max_actions = int(level.cards[0][level.cards[0].index("max_actions") + 1])
                        music = level.music



                        save_stats(game_data, os.path.join(get_appdata_path("Risktakers"), "Prototip_game_data.py"))
                        menu = 0
                    elif button[2] == "current_level":
                        game_data = load_stats("Prototip_game_data.py", create_game_data, "Risktakers")
                        game_data2 = game_data.copy()
                        music[0].stop()
                        level = my_import(game_data["level"])
                        level.did_actions = 0
                        level.lst_i = game_data["scene"]
                        game_reset(list_of_levels)
                        level.create(game_data)
                        level.max_actions = int(level.cards[level.lst_i][level.cards[level.lst_i].index("max_actions") + 1])
                        music = level.music
                        menu = 0
                    elif button[2] == "settings":
                        level = my_import("level_settings")
                        settings_menu = 1
                        menu = 0
                    elif button[2] == "quit":
                        run = 0


            elif settings_menu:
                if level.button_exit[1].collidepoint(event.pos):
                    settings_menu = 0
                    menu = 1
                    enter = 0
                    level = my_import("level_menu")
                if rect1.collidepoint(event.pos):
                    enter = 1
            elif esc_pressed:
                if button_continue[1].collidepoint(event.pos):
                    esc_pressed = 0
                elif button_save[1].collidepoint(event.pos):
                    game_data2["level"] = level.level
                    game_data2["scene"] = level.lst_i
                    save_stats(game_data2, os.path.join(get_appdata_path("Risktakers"), "Prototip_game_data.py"))
                elif button_menu[1].collidepoint(event.pos):
                    music[0].stop()
                    level = my_import("level_menu")
                    music = level.music
                    esc_pressed = 0
                    menu = 1

            else:
                for i in level.cards[level.lst_i][:level.cards[level.lst_i].index("did_actions")]:

                    if level.did_actions < level.max_actions and 1 not in i and i[1].collidepoint(event.pos) and check_money(game_data, i):
                        pg.mixer.Sound(get_path("click.wav")).play()
                        if i[2] == "text" and 1 not in i and check_money(game_data, i):
                            i.append(1)
                            level.did_actions += 1
                        if "effect" in i and "used" not in i and check_money(game_data, i):
                            if "next_level" in i:
                                level.did_actions = level.max_actions
                                if "change_next_level" in i:
                                    level.next_level = i[9]
                                    level.did_actions = level.max_actions
                                    level.lst_i = len(level.cards) - 1
                            else:
                                game_data[i[i.index("effect") + 1]] += int(i[i.index("effect") + 2])
                                i.append("used")
                        if "effect2" in i and "used2" not in i and check_money(game_data, i):
                            if "next_level" in i:
                                level.did_actions = level.max_actions
                                if "change_next_level" in i:
                                    level.next_level = i[9]
                                    level.did_actions = level.max_actions
                                    level.lst_i = len(level.cards) - 1
                            else:
                                game_data[i[i.index("effect2") + 1]] += int(i[i.index("effect2") + 2])
                                i.append("used2")


                        if "do_create" in i:
                            do_create = 1
                        if "scene" in level.cards[level.lst_i]:
                            scene = int(level.cards[level.lst_i][level.cards[level.lst_i].index("scene") + 1])
                        if "effect_next_scene" in i:
                            level.did_actions = level.max_actions
                            lst_i = int(i[i.index("effect_next_scene") + 1])
                        if "effect_next_level" in i:
                            level.did_actions = level.max_actions
                            if "change_next_level" in i:
                                level.next_level = i[i.index("change_next_level") + 1]
                                level.did_actions = level.max_actions
                                level.lst_i_mx = level.lst_i + 1
                        elif "effect_back_scene" in i:
                            lst_i = int(i[i.index("effect_back_scene") + 1])
                            level.did_actions = level.max_actions
                            did = int(i[i.index("effect_back_scene") + 2])
                            mx = int(i[i.index("effect_back_scene") + 3])
                        if "final" in level.cards[0][0]:
                            level.did_actions = 1
                            menu = 1
                            music[0].stop()
                            level = my_import("level_menu")
                            music = level.music

                        if not check_hearts(game_data):
                            level.lst_i_mx = level.lst_i + 1
                            level.next_level = "menu_of_dead"
                            if death:
                                music[0].stop()
                                level = my_import("level_menu")
                                music = level.music
                                menu = 1
                                death = 0
                            else:
                                death = 1
                                level.did_actions = level.max_actions
                                scene = 0
                        break

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3 and not menu and not esc_pressed and not settings_menu:
            if do_create:
                level.create(game_data)
                do_create = 0
            if lst_i:
                level.lst_i += lst_i
                if mx:
                    level.did_actions = did
                    level.max_actions = mx
                    mx = 0
                else:

                    level.did_actions = int(level.cards[level.lst_i][level.cards[level.lst_i].index("did_actions") + 1])
                    level.max_actions = int(level.cards[level.lst_i][level.cards[level.lst_i].index("max_actions") + 1])
                lst_i = 0


            elif level.did_actions == level.max_actions:
                level.lst_i += 1
                if level.lst_i == level.lst_i_mx:
                    level = my_import(level.next_level)
                    level.create(game_data)
                    if scene:
                        level.lst_i = scene
                        scene = 0
                    else:
                        level.lst_i = 0
                        level.did_actions = 0
                        level.max_actions = int(level.cards[level.lst_i][level.cards[level.lst_i].index("max_actions") + 1])

                    if music[1] != level.music[1]:
                        music[0].stop()
                        music = level.music



                    game_data2 = game_data.copy()
                else:
                    level.did_actions = 0
                    level.max_actions = int(level.cards[level.lst_i][level.cards[level.lst_i].index("max_actions") + 1])
                    game_data2 = game_data.copy()
        elif not menu and event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            if not esc_pressed:
                esc_pressed = 1
            else:
                esc_pressed = 0



    screen.blit(level.background_img, background_img_rect)
    if not menu and not settings_menu:
        if level.cards[0][0][-1] == "final":
            card_surf = pg.Surface((2016, 1152))
            lst = [i for i in level.cards[0][0][3] if i != '']
            rect2 = level.font.render(max(level.cards[0][0][3], key=len), False, WHITE, None).get_rect()
            height = rect2[3]
            SIZE2 = (rect2[2], len(lst) * height)
            card_surf.blit(level.background_img, background_img_rect)
            y = 0
            card_surf2 = pg.Surface(SIZE2)
            card_surf2.fill(BLACK)
            card_surf2.set_alpha(120)
            rect2 = card_surf2.get_rect()
            rect2.center = SIZE[0] // 2, (len(level.cards[0][0][3]) - len(lst) + (0.25 + 8 - len([i for i in level.cards[0][0][3] if i == '']) + 1)) * height
            card_surf.blit(card_surf2, rect2)
            for i in level.cards[0][0][3]:
                i = level.font.render(i, False, WHITE, None)
                i_rect = i.get_rect()
                i_rect.center = SIZE[0] // 2, y
                card_surf.blit(i, i_rect)
                y += level.size * 1.1


            screen.blit(card_surf, level.cards[0][0][1])




        elif len(level.cards[level.lst_i][:level.cards[level.lst_i].index("did_actions")]) == 1:

            if 1 in level.cards[level.lst_i][0]:
                card_surf = pg.Surface((448, 556))
                card_surf.fill(BROWN)
                y = 0
                for i in level.cards[level.lst_i][0][3]:
                    card_surf.blit(font.render(i, False, WHITE, None), (0, y))
                    y += 35
                screen.blit(card_surf, level.cards[level.lst_i][0][1])
            else:
                level.cards[level.lst_i][0][1].center = SIZE[0] // 2, SIZE[1] // 2
                screen.blit(level.cards[level.lst_i][0][0], level.cards[level.lst_i][0][1])
                if "action" in level.cards[level.lst_i][0]:
                    action_rect = level.cards[level.lst_i][0][5].get_rect()
                    action_rect.center = level.cards[level.lst_i][0][1].center[0], level.cards[level.lst_i][0][1][3] + 4
                    screen.blit(level.cards[level.lst_i][0][5], action_rect)
            pg.draw.rect(screen, GOLDEN, (level.cards[level.lst_i][0][1][0] - 3, level.cards[level.lst_i][0][1][1] - 3,
                                                level.cards[level.lst_i][0][1][2] + 3, level.cards[level.lst_i][0][1][3] + 3), 3)

        elif len(level.cards[level.lst_i][:level.cards[level.lst_i].index("did_actions")]) == 2:
            x = 250
            for i in range(2):
                x *= -1
                if 1 in level.cards[level.lst_i][i]:
                    card_surf = pg.Surface((448, 556))
                    card_surf.fill(BROWN)
                    y = 0
                    for h in level.cards[level.lst_i][i][3]:
                        card_surf.blit(font.render(h, False, WHITE, None), (0, y))
                        y += 35
                    screen.blit(card_surf, level.cards[level.lst_i][i][1])
                else:
                    level.cards[level.lst_i][i][1].center = SIZE[0] // 2 + x, SIZE[1] // 2
                    screen.blit(level.cards[level.lst_i][i][0], level.cards[level.lst_i][i][1])
                    if "action" in level.cards[level.lst_i][i]:
                        action_rect = level.cards[level.lst_i][i][5].get_rect()
                        action_rect.center = level.cards[level.lst_i][i][1].center[0], level.cards[level.lst_i][i][1][3] + 200
                        screen.blit(level.cards[level.lst_i][i][5], action_rect)
                pg.draw.rect(screen, GOLDEN, (level.cards[level.lst_i][i][1][0] - 3, level.cards[level.lst_i][i][1][1] - 3,
                                                    level.cards[level.lst_i][i][1][2] + 3, level.cards[level.lst_i][i][1][3] + 3), 3)


        elif len(level.cards[level.lst_i][:level.cards[level.lst_i].index("did_actions")]) == 3:
            for i in range(3):
                if 1 in level.cards[level.lst_i][i]:
                    card_surf = pg.Surface((448, 556))
                    card_surf.fill(BROWN)
                    y = 0
                    for h in level.cards[level.lst_i][i][3]:
                        card_surf.blit(font.render(h, False, WHITE, None), (0, y))
                        y += 35
                    screen.blit(card_surf, level.cards[level.lst_i][i][1])
                else:
                    level.cards[level.lst_i][i][1].center = SIZE[0] // 2 + (-500 + 500 * i), SIZE[1] // 2
                    screen.blit(level.cards[level.lst_i][i][0], level.cards[level.lst_i][i][1])
                    if "action" in level.cards[level.lst_i][i]:
                        action_rect = level.cards[level.lst_i][i][5].get_rect()
                        action_rect.center = level.cards[level.lst_i][i][1].center[0], level.cards[level.lst_i][i][1][3] + 200
                        screen.blit(level.cards[level.lst_i][i][5], action_rect)
                pg.draw.rect(screen, GOLDEN, (level.cards[level.lst_i][i][1][0] - 3, level.cards[level.lst_i][i][1][1] - 3,
                                                     level.cards[level.lst_i][i][1][2] + 3, level.cards[level.lst_i][i][1][3] + 3), 3)
        if "final" not in level.cards[level.lst_i][0]:
            for i in range(1, game_data["hearts"] + 1):
                draw_heart(screen, SIZE[0] - 50 * i, 40)
            money = font.render(str(game_data["money"]) + " $", False, WHITE, None)
            money_rect = money.get_rect()
            money_rect.center = SIZE[0] - 50, 80
            screen.blit(money, money_rect)

        if esc_pressed:
            esc_menu = (pg.Surface((SIZE[0], SIZE[1])))
            esc_menu.set_alpha(150)
            esc_menu_rect = esc_menu.get_rect()
            esc_menu_rect.center = SIZE[0] // 2, SIZE[1] // 2
            esc_menu.fill(BLACK)
            font2 = pg.font.SysFont("arial", 40, False, False)
            button_continue = [font2.render("Продолжить", False, WHITE, None),
                               font2.render("Продолжить", False, WHITE, None).get_rect()]
            button_continue[1].center = SIZE[0] // 2, SIZE[1] // 2 - 60
            esc_menu.blit(button_continue[0], button_continue[1])

            button_save = [font2.render("Сохранить", False, WHITE, None),
                               font2.render("Сохранить", False, WHITE, None).get_rect()]
            button_save[1].center = SIZE[0] // 2, SIZE[1] // 2
            esc_menu.blit(button_save[0], button_save[1])

            button_menu = [font2.render("Главное меню", False, WHITE, None),
                               font2.render("Главное меню", False, WHITE, None).get_rect()]
            button_menu[1].center = SIZE[0] // 2, SIZE[1] // 2 + 60
            esc_menu.blit(button_menu[0], button_menu[1])

            screen.blit(esc_menu, esc_menu_rect)
    elif settings_menu:
        level.button_exit[1].center = 150, 50
        screen.blit(level.button_exit[0], level.button_exit[1])
        button = level.font3.render("Громкость:  " + str(s) + "%", False, WHITE, None)
        rect1 = button.get_rect()
        rect1.center = SIZE[0] // 2, SIZE[1] // 2
        screen.blit(button, rect1)

    else:
        level.buttons[0][1].center = SIZE[0] // 2, SIZE[1] // 2 - 150
        screen.blit(level.buttons[0][0], level.buttons[0][1])

        level.buttons[1][1].center = SIZE[0] // 2, SIZE[1] // 2 - 50
        screen.blit(level.buttons[1][0], level.buttons[1][1])

        level.buttons[2][1].center = SIZE[0] // 2, SIZE[1] // 2 + 50
        screen.blit(level.buttons[2][0], level.buttons[2][1])

        level.buttons[3][1].center = SIZE[0] // 2, SIZE[1] // 2 + 150
        screen.blit(level.buttons[3][0], level.buttons[3][1])

    pg.display.update()
    clock.tick(60)

config["volume"] = s
save_stats(config, os.path.join(get_appdata_path("Risktakers"), "configuration.py"))
pg.mixer.quit()
pg.quit()