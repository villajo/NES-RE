import pygame as pg
import pygame.joystick as gamepad
from pygame.locals import *

running = True

WHITE = (255,255,255)

rooms = {
    '01': {
        'name': 'Main Hall',
        'door_n': '',
        'door_s': '',
        'door_e': '',
        'door_w': '',
        'start': (372,519),
    }
}

def load_room(room):
    return rooms['01']


def init():
    background_colour = (0,0,0)
    (width, height) = (768, 720)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Resident Evil - Proto')
    screen.fill(background_colour)
    pg.display.flip()
    return screen

def title(screen):

    option_selected = 0

    #logo_img_1 = pg.image.load('res/RE Logo.png')
    pg.font.init()
    logo_font = pg.font.SysFont('dincondensed', 100)
    logo = logo_font.render("RESIDENT EVIL", False, (255, 0, 0))




    print(pg.font.get_fonts())



    title_screen = True
    while title_screen:

        menu_font = pg.font.SysFont('helvetica', 30)

        if option_selected == 0:
            menu_start = menu_font.render("- Start", False, (255, 255, 255))
            menu_network = menu_font.render("  RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("  Continue", False, (255, 255, 255))
            menu_options = menu_font.render("  Options", False, (255, 255, 255))
        if option_selected == 1:
            menu_start = menu_font.render("  Start", False, (255, 255, 255))
            menu_network = menu_font.render("- RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("  Continue", False, (255, 255, 255))
            menu_options = menu_font.render("  Options", False, (255, 255, 255))
        if option_selected == 2:
            menu_start = menu_font.render("  Start", False, (255, 255, 255))
            menu_network = menu_font.render("  RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("- Continue", False, (255, 255, 255))
            menu_options = menu_font.render("  Options", False, (255, 255, 255))
        if option_selected == 3:
            menu_start = menu_font.render("  Start", False, (255, 255, 255))
            menu_network = menu_font.render("  RE:Net game", False, (255, 255, 255))
            menu_continue = menu_font.render("  Continue", False, (255, 255, 255))
            menu_options = menu_font.render("- Options", False, (255, 255, 255))



        screen.blit(logo, (160, 130))
        screen.blit(menu_start, (260, 300))
        screen.blit(menu_network, (260, 330))
        screen.blit(menu_continue, (260, 360))
        screen.blit(menu_options, (260, 4200))
        #screen.blit()

        pg.display.flip()
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            print("left")
            title_screen = False
        if keys[pg.K_RIGHT]:
            print("right")
        if keys[pg.K_UP]:
            print("up")
        if keys[pg.K_DOWN]:
            if option_selected < 3:
                option_selected += 1
            if option_selected == 3:
                option_selected = 0


    return "Test"


def game(screen, opts):
    player_sprite = pg.image.load('res/green.png')
    attack_sprite = pg.image.load('res/red.png')
    #joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
    #player1_control = pygame.joystick.Joystick(0)
    #player1_control.init()

    #print(joysticks)
    #print(player1_control)
    game = True

    player_loc_x = 0
    player_loc_y = 0

    bg = pg.image.load("res/mh_01.png")

    #Debug Location

    font = pg.font.Font('freesansbold.ttf', 32)

    while game:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game = False
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            print("left")
            if player_loc_x > 0:
                player_loc_x = player_loc_x - 3
        if keys[pg.K_RIGHT]:
            if player_loc_x <= 768 - 16:
                player_loc_x = player_loc_x + 3
        if keys[pg.K_UP]:
            print("up")
            if player_loc_y > 0:
                player_loc_y = player_loc_y - 3
        if keys[pg.K_DOWN]:
            print("down")
            if player_loc_y <= 720 - 16:
                player_loc_y = player_loc_y + 3

        screen.fill((0, 0, 0))
        player_loc = font.render('X: ' + str(player_loc_x) + ' Y: ' + str(player_loc_y), True, WHITE)
        textRect = player_loc.get_rect()
        textRect.topright = (768, 0)


        screen.blit(bg, (0,0))
        screen.blit(player_sprite,(player_loc_x, player_loc_y))
        screen.blit(player_loc, textRect)


        pg.display.flip()
        pg.display.update()

def main():
    screen = init()
    opts = title(screen)
    game(screen, opts)


if __name__ == '__main__':
    pg.init()
    gamepad.init()
    print(gamepad.get_init())
    print(gamepad.get_count())
    joysticks = [gamepad.Joystick(x) for x in range(gamepad.get_count())]
    main()