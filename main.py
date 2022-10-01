import pygame as pg
import pygame.joystick as gamepad
import data as data

running = True

W_SPEED = 1
R_SPEED = 3

WHITE = (255, 255, 255)

u_boundaries = ()
d_boundaries = ()
l_boundaries = ()
r_boundaries = ()


def get_room_bounds(x, y, direction):
    if direction == 'UP':
        for i in range(0, len(u_boundaries)):
            if u_boundaries[i]:
                for j in range(0, 64):
                    if player_state == "WALK":
                        if x + j + W_SPEED in range(u_boundaries[i][0][0], u_boundaries[i][1][0]):
                            if u_boundaries[i][0][1] <= y <= u_boundaries[i][1][1]:
                                return True, u_boundaries[i][2]
                    if player_state == "RUN":
                        if x + j + R_SPEED in range(u_boundaries[i][0][0], u_boundaries[i][1][0]):
                            if u_boundaries[i][0][1] <= y <= u_boundaries[i][1][1]:
                                return True, u_boundaries[i][2]
        return False, 'None'
    if direction == 'RIGHT':
        for i in range(0, len(r_boundaries)):
            if r_boundaries[i]:
                if player_state == "WALK":
                    if x + 64 == r_boundaries[i][0][0]:
                        if r_boundaries[i][0][1] <= y <= r_boundaries[i][1][1]:
                            return True, r_boundaries[i][2]
                if player_state == "RUN":
                    if x + 64 + R_SPEED == r_boundaries[i][0][0]:
                        if r_boundaries[i][0][1] <= y <= r_boundaries[i][1][1]:
                            return True, r_boundaries[i][2]
        return False, 'None'
    if direction == 'LEFT':
        for i in range(0, len(l_boundaries)):
            if l_boundaries[i]:
                if player_state == "WALK":
                    if x == l_boundaries[i][0][0]:
                        if l_boundaries[i][0][1] <= y <= l_boundaries[i][1][1]:
                            return True, l_boundaries[i][2]
                if player_state == "RUN":
                    if x - R_SPEED == l_boundaries[i][0][0]:
                        if l_boundaries[i][0][1] <= y <= l_boundaries[i][1][1]:
                            return True, l_boundaries[i][2]
        return False, 'None'
    if direction == 'DOWN':
        for i in range(0, len(d_boundaries)):
            if d_boundaries[i]:
                if player_state == "WALK":
                    print("WALK")
                if player_state == "RUN":
                    print("RUN")
        return False, 'None'

def init():
    background_colour = (0, 0, 0)
    (width, height) = (768, 720)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Resident Evil - Proto')
    screen.fill(background_colour)
    pg.display.flip()
    return screen


def title(screen):
    option_selected = 0
    pg.font.init()
    logo_font = pg.font.SysFont('dincondensed', 100)
    logo = logo_font.render("RESIDENT EVIL", False, (255, 0, 0))

    title_screen = True
    while title_screen:

        menu_font = pg.font.SysFont('helvetica', 30)

        if option_selected == 0:
            menu_start = menu_font.render("Start", False, (220, 220, 220))
            menu_network = menu_font.render("RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("Continue", False, (255, 255, 255))
            menu_options = menu_font.render("Options", False, (255, 255, 255))
        if option_selected == 1:
            menu_start = menu_font.render("Start", False, (255, 255, 255))
            menu_network = menu_font.render("RE:Net game", False, (220, 220, 220))
            menu_continue = menu_font.render("Continue", False, (255, 255, 255))
            menu_options = menu_font.render("Options", False, (255, 255, 255))
        if option_selected == 2:
            menu_start = menu_font.render("Start", False, (255, 255, 255))
            menu_network = menu_font.render("RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("Continue", False, (220, 220, 220))
            menu_options = menu_font.render("Options", False, (255, 255, 255))
        if option_selected == 3:
            menu_start = menu_font.render("Start", False, (255, 255, 255))
            menu_network = menu_font.render("RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("Continue", False, (255, 255, 255))
            menu_options = menu_font.render("Options", False, (220, 220, 220))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if option_selected <= 3:
                        option_selected += 1
                    if option_selected == 4:
                        option_selected = 0
                if event.key == pg.K_UP:
                    if option_selected >= 0:
                        option_selected -= 1
                    if option_selected < 0:
                        option_selected = 3
                if event.key == pg.K_RETURN:
                    if option_selected == 0:
                        return "GAME"

        screen.fill((0, 0, 0))
        screen.blit(logo, (160, 130))
        screen.blit(menu_start, (300, 300))
        screen.blit(menu_network, (300, 330))
        screen.blit(menu_continue, (300, 360))
        screen.blit(menu_options, (300, 390))

        pg.display.flip()
        pg.display.update()

    return "None"


def game(screen, opts):
    global u_boundaries, d_boundaries, l_boundaries, r_boundaries
    u_boundaries, d_boundaries, l_boundaries, r_boundaries, room_img = data.load_area_data("01", "mansion")
    player_sprite = pg.image.load('res/green.png')
    action_sprite = pg.image.load('res/red.png')
    game = True

    global player_state

    player_loc_x = 360
    player_loc_y = 460

    bg = pg.image.load("res/" + room_img + ".png")
    font = pg.font.Font('freesansbold.ttf', 32)

    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            player_state = "RUN"
        if not keys[pg.K_a]:
            player_state = "WALK"


        if keys[pg.K_LEFT]:
            if player_loc_x > 0:
                boundary, object_type = get_room_bounds(player_loc_x, player_loc_y, 'LEFT')
                if not boundary:
                    if player_state is "WALK":
                        player_loc_x = player_loc_x - W_SPEED
                    if player_state is "RUN":
                        player_loc_x = player_loc_x - R_SPEED
        if keys[pg.K_RIGHT]:
            if player_loc_x <= 768 - 64:
                boundary, object_type = get_room_bounds(player_loc_x, player_loc_y, 'RIGHT')
                if not boundary:
                    if player_state is "WALK":
                        player_loc_x = player_loc_x + W_SPEED
                    if player_state is "RUN":
                        player_loc_x = player_loc_x + R_SPEED
        if keys[pg.K_UP]:
            if player_loc_y > 0:
                boundary, object_type = get_room_bounds(player_loc_x, player_loc_y, 'UP')
                if not boundary:
                    if player_state is "WALK":
                        player_loc_y = player_loc_y - W_SPEED
                    if player_state is "RUN":
                        player_loc_y = player_loc_y - R_SPEED
        if keys[pg.K_DOWN]:
            if player_loc_y <= 720 - 128:
                boundary, object_type = get_room_bounds(player_loc_x, player_loc_y, 'DOWN')
                if not boundary:
                    if player_state is "WALK":
                        player_loc_y = player_loc_y + W_SPEED
                    if player_state is "RUN":
                        player_loc_y = player_loc_y + R_SPEED

        screen.fill((0, 0, 0))
        player_loc = font.render('X: ' + str(player_loc_x) + ' Y: ' + str(player_loc_y), True, WHITE)
        textRect = player_loc.get_rect()
        textRect.topright = (768, 0)
        screen.blit(bg, (0, 0))
        screen.blit(player_sprite, (player_loc_x, player_loc_y))
        screen.blit(player_loc, textRect)
        pg.display.flip()
        pg.display.update()


def main():
    running = True
    selection = ''
    screen = init()
    while running:
        if selection == 'GAME':
            game(screen, "Test")
        elif selection == 'OPTIONS':
            print("Nothing yet")
            selection = ''
        else:
            selection = title(screen)


if __name__ == '__main__':
    pg.init()
    joysticks = [gamepad.Joystick(x) for x in range(gamepad.get_count())]
    main()
