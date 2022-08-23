import pygame
from settings import *

pygame.font.init()

f1 = pygame.font.Font(None, 36)
num100 = f1.render('100', True, (255, 255, 255))
num200 = f1.render('200', True, (255, 255, 255))
num300 = f1.render('300', True, (255, 255, 255))
num400 = f1.render('400', True, (255, 255, 255))
num0 = f1.render('0', True, (255, 255, 255))
course = f1.render('Цена: ' + str(price / 100) + ' долларов', True, (255, 255, 255))

f2 = pygame.font.Font(None, 100)
numOfMoney = f2.render(str(money / 100) + ' долларов', True, (255, 255, 255))
numOfObl = f2.render(str(obl) + ' акций', True, (255, 255, 255))
buy = f2.render('купить акцию', True, (255, 255, 255))
sell = f2.render('продать акцию', True, (255, 255, 255))

f3 = pygame.font.Font(None, 200)
menuText = f3.render('Lite Trade', True, (255, 255, 255))

f4 = pygame.font.Font(None, 100)
startText = f4.render('Нажмите Лкм чтобы начать игру', True, (255, 255, 255))
endText = f4.render('Нажмите на колесико чтобы закончить', True, (255, 255, 255))