import pygame
import random

pygame.init()
win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#win settings
width, height = pygame.display.get_surface().get_size()
screenWidth = width - 50
screenHeight = 900

#variables
price = 10000
x = 0
y = screenHeight - (screenHeight / (400 * 100)) * price
size = 5

blockCoefficient = 4
blockX = 0
blockY = 0

r = 255
g = 0
b = 0

r1 = 50
g1 = 50
b1 = 50

r2 = 50
g2 = 50
b2 = 50

money = 50000
obl = 0

#other settings
run = True
started = True
menu = True