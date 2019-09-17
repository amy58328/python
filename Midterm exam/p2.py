import pygame
import time
import random
 
pygame.init()

screen= pygame.display.set_mode((1000,650))
pygame.display.set_caption('p2')
clock = pygame.time.Clock()

crashed = False
black = (0,0,0)

bullet_show = pygame.image.load("bull.png")

bullet_show = pygame.transform.scale(bullet_show,(50,50))
bullet_show2 = pygame.transform.scale(bullet_show,(100,100))

class bul:
	def _init_(self):
		self.x = 0 
		self.y = 0 


x = []
y = []
	
while not crashed:


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		screen.fill(black)
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		screen.blit(bullet_show,(mouse[0],mouse[1]))

		if click[0] == 1:
			x.append(mouse[0])
			y.append(mouse[1])

		for i in range(0,len(x)):
			screen.blit(bullet_show2,(x[i],y[i]))



	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()