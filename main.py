import pygame
import random
from settings import *
from functions import *

pygame.display.flip()

while run:
	if menu:
		drawMenu()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					menu = False
		pygame.display.update()
	if menu == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 2:
					run = False
				if event.button == 1:
					if event.pos[0] < screenWidth / 3 and event.pos[1] > screenHeight:
						if money > price:
							money = money - price
							obl += 1
							r1 = 25
							g1 = 25
							b1 = 25
							pygame.draw.rect(win, (0, 255, 0), (x, screenHeight - 15, 5, 15))
					if event.pos[0] > screenWidth / 3 and event.pos[0] < screenWidth / 3 * 2 and event.pos[1] > screenHeight:
						if obl > 0:
							money = money + price
							obl -= 1
							r2 = 25
							g2 = 25
							b2 = 25
					

		if started:
			drawBack(blockX, blockY, screenWidth, screenHeight, blockCoefficient)
			started = False

		draw(x, y)
		drawCost()
		drawButtons(money, obl, r1, b1, g1, r2, g2, b2)
		#drawButtons(money, obl)
		drawPrice(price)
	 
		x = x + 0.1
		price = random.randint(price - size * 50, price + size * 50)

		y = screenHeight - (screenHeight / (400 * 100)) * price

		if x > screenWidth:
			started = True
			x = 0

		if price < 0:
			price = 0
			#started = True

		if price > 40000:
			price = 40000
			#started = True

		r1 = 50
		g1 = 50
		b1 = 50

		r2 = 50
		g2 = 50
		b2 = 50

		pygame.display.update()