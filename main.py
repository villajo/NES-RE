import pygame
import sys

running = True

def init():
    background_colour = (0,0,0)
    (width, height) = (768, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Resident Evil - Proto')
    screen.fill(background_colour)
    pygame.display.flip()


def title(): 
    title = True
    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title = False  

def game():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

def main():
    init()
    game()




if __name__ == '__main__':
    main()