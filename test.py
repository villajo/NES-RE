import pygame as pg
import pygame.joystick as gamepad

gamepad.init()
print(gamepad.get_init())
print(gamepad.get_count())
joysticks = [gamepad.Joystick(x) for x in range(gamepad.get_count())]