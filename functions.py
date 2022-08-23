import pygame
import random
from settings import *
from text import *

def draw(x, y):
	pygame.draw.rect(win, (r, g, b), (x - size / 2, y - size / 2, size, size))

def drawBack(blockX, blockY, screenWidth, screenHeight, blockCoefficient):
	win.fill((50, 50, 50))
	while blockY < screenHeight:
		while blockX < screenWidth:
			pygame.draw.rect(win, (150, 150, 150), (blockX, blockY, screenWidth / blockCoefficient, screenHeight / blockCoefficient), 1)
			blockX = blockX + screenWidth / blockCoefficient
		blockY = blockY + screenHeight / blockCoefficient
		blockX = 0
	

def drawCost():
	win.blit(num400, (screenWidth, 0))
	win.blit(num300, (screenWidth, screenHeight / blockCoefficient - 15))
	win.blit(num200, (screenWidth, screenHeight / blockCoefficient * 2 - 15))
	win.blit(num100, (screenWidth, screenHeight / blockCoefficient * 3 - 15))
	win.blit(num0, (screenWidth, screenHeight / blockCoefficient * 4 - 15))
	

def drawButtons(money, obl, r1, b1, g1, r2, g2, b2):
	pygame.draw.rect(win, (50, 50, 50), (0, screenHeight, screenWidth, height))
	numOfMoney = f2.render(str(money / 100) + ' долларов', True, (255, 255, 255))
	numOfObl = f2.render(str(obl) + ' акций', True, (255, 255, 255))
	pygame.draw.rect(win, (r1, g1, b1), (0, screenHeight, screenWidth / 3, height - screenHeight))
	pygame.draw.rect(win, (r2, g2, b2), (screenWidth / 3, screenHeight, screenWidth / 3, height - screenHeight))
	pygame.draw.rect(win, (255, 255, 255), (0, screenHeight, screenWidth / 3, height - screenHeight), 5)
	pygame.draw.rect(win, (255, 255, 255), (screenWidth / 3, screenHeight, screenWidth / 3, height - screenHeight), 5)
	pygame.draw.rect(win, (255, 255, 255), (screenWidth / 3 * 2, screenHeight, screenWidth / 3, height - screenHeight), 5)
	win.blit(numOfMoney, (screenWidth / 3 * 2 + 5, screenHeight + 15))
	win.blit(numOfObl, (screenWidth / 3 * 2 + 5, screenHeight + 85))
	win.blit(buy, (5, screenHeight + 50))
	win.blit(sell, (screenWidth / 3 + 5, screenHeight + 50))
def drawMenu():
	win.fill((50, 50, 50))
	win.blit(menuText, (100, 100))
	win.blit(startText, (width / 3, (height / 2) + 50))
	win.blit(endText, (width / 4, (height / 2) + 150))
def drawPrice(price):
	course = f1.render('Цена: ' + str(price / 100) + ' долларов', True, (255, 255, 255))
	text_width = course.get_width()
	text_height = course.get_height()
	pygame.draw.rect(win, (0, 0, 0), (0, 0, text_width, text_height))
	pygame.draw.rect(win, (255, 255, 255), (0, 0, text_width, text_height), 1)
	win.blit(course, (0, 0))