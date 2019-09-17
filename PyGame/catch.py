import pygame
import time
import random

pygame.init()

display_height = 600
display_width = 800 
text_color = (255,0,0)
backgroung = (0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

##setting##################################################
basket = pygame.image.load('basket.png')
apple = pygame.image.load("apple.png")
bug = pygame.image.load("bug.png")
apple_tree = pygame.image.load("apple_tree.jpg")
x_move = 0
y_move = 0
basket_width = 150
apple_width = 100
apple_x = random.randrange(0,display_width)
apple_y = 0
bug_width = 50
bug_x = random.randrange(0,display_width)
bug_y = 0
n = random.randrange(0,2)
grade = 0
x = 400
y = 450
error = 50
##subroutine##################################################
def basket_b(x,y):
	gameDisplay.blit(apple_tree,(0,0))
	gameDisplay.blit(basket, (x,y))

def apple_b():
	global apple_y, apple_x,n,bug_x,bug_y
	bug_y = 0
	bug_x = 0
	apple_y += 3
	gameDisplay.blit(apple, (apple_x,apple_y))
	if apple_y > 600 :
		apple_x = random.randrange(0,display_width)
		apple_y = 0
		
def bug_b():
	global bug_x , bug_y ,n,apple_y,apple_x
	apple_x = 0 
	apple_y = 0
	bug_y += 3
	gameDisplay.blit(bug, (bug_x,bug_y))
	if bug_y > 600 :
		bug_x = random.randrange(0,display_width)
		bug_y = 0
		n = random.randrange(0,2)

def reset():
	global bug_y,apple_y,n,apple_x,bug_x,x,y
	x = 400
	y = 450
	n = random.randrange(0,2)
	apple_x = random.randrange(0,display_width)
	bug_x = random.randrange(0,display_width)
	apple_y = 0
	bug_y = 0
	time.sleep(0.75)

def chang():
	global x_move,y_move,x,y
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_c:
			x_move = -5
		elif event.key == pygame.K_RIGHT:
			x_move = 5
		elif event.key == pygame.K_UP:
			y_move = -5
		elif event.key == pygame.K_DOWN:
			y_move = 5
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			x_move = 0
		elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			y_move = 0
	
def crash():
	n = 0
	if x > display_width - basket_width +error or x < -50 :
		n = 1
		message_display('You Crashed',(display_width/2),(display_height/2),115,1)
	elif y < -50 or y > display_height - basket_width +error:
		n = 1
		message_display('You Crashed',(display_width/2),(display_height/2),115,1)
	return n

def eat_apple():
	global grade,apple_x
	if apple_x >= x - apple_width + error and apple_x <= x + basket_width - error :
		if apple_y >= y - apple_width + error and apple_y <= y + basket_width - error:
			grade += 1
			reset()

def eat_bug():
	global grade
	if bug_x >= x - bug_width + error and bug_x <= x + basket_width - error :
		if bug_y >= y - bug_width + error and bug_y <= y + basket_width - error:
			grade -= 1
			reset()	

	
def text_objects(text, font):
	textSurface = font.render(text, True, text_color)
	return textSurface, textSurface.get_rect()

def message_display(text,x_,y_ , size , crash_):
	largeText = pygame.font.Font('LucidaBrightDemiBold.ttf',size)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((x_),(y_))
	gameDisplay.blit(TextSurf, TextRect)

	if crash_ == 1 :
		pygame.display.update()
		reset()
##main function############################################################

def main():
	global event,x,y,grade
	
	reset()
	grade = 0
	crashed = False

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				crashed = True

		chang()
		x += x_move
		y += y_move
		basket_b(x,y)
		if n == 0:
			apple_b()

		elif n == 1:
			bug_b()

		if crash() :
			crashed = True
		
		eat_apple()
		eat_bug()	
		message_display('grade:' + str(grade),120,50,40,0)
 

		pygame.display.update()
		clock.tick(60)
		
main()
pygame.quit()
quit()