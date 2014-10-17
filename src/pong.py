import pygame
from pygame.locals import *
import sys

DISPLAY = 800,600
GREEN = 25,200,50
WHITE = 255,255,255
BLACK = 0,0,0
YELLOW = 255,255,0
BLUE = 0,0,255
RED = 255,0,0

BAR_VEL = 25.


bar1 = pygame.Surface((15,50))
bar2 = pygame.Surface((15,50))
circ_sur = pygame.Surface((15,15))
clock = pygame.time.Clock()

class background:
	def __init__(self,dSize):
		self.image = pygame.Surface(dSize)
		self.image.fill(GREEN)
		netWidth = dSize[0]/80
		self.net = pygame.Rect(0,0,netWidth,dSize[1])
		self.net.centerx = dSize[0]/2
		pygame.draw.rect(self.image,WHITE,self.net)

	def draw(self,display):
		display.blit(self.image,(0,0))
class PhonePong:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(DISPLAY)
		pygame.display.set_caption("MyGame")
		self.green = background(DISPLAY)
		self.screen.fill(BLACK)
		self.green.draw(self.screen)
		# Part 2: Creating 2 bars and a ball:
		bar1.fill((BLUE))
		bar2.fill((RED))
		circ = pygame.draw.circle(circ_sur,(YELLOW),(15/2,15/2),15/2)
		self.circle = circ_sur.convert()
		self.circle.set_colorkey((BLACK))
		
	def __del__(self):
		print "exit signal received"

	def run(self):
		self.bar1_x = 10.
		self.bar1_y = 275.
		self.bar1_move = 0.
		self.bar2_x = 775.
		self.bar2_y = 275.
		self.bar2_move = 0.
		self.circle_x = 307.5
		self.circle_y = 300.
		self.ball_velx = 100.
		self.ball_vely = 100.
		self.bar1_score = 0
		self.bar2_score = 0
		while True:
			self.time_passed = clock.tick(10)
			self.handleEvents()
			self.fps=clock.get_fps()
			self.handleText()
			pygame.display.flip()

	def handleText(self):
		myfont = pygame.font.SysFont("Verdana",20)
		label = myfont.render("PhonePong"+"(fps: {:.1f})".format(self.fps),1,YELLOW)
		self.screen.blit(label,(10,10))

	def handleEvents(self):
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_UP:
					self.bar1_move = -BAR_VEL
				elif event.key == K_DOWN:
					self.bar1_move = BAR_VEL
			elif event.type == KEYUP:
				if event.key == K_UP:
					self.bar1_move = 0.
				elif event.key == K_DOWN:
					self.bar1_move = 0.
		# Movments upgrade:
		self.bar1_y += self.bar1_move
		self.bar2_y += self.bar1_move

		time_sec = self.time_passed / 1000.

		self.circle_x += self.ball_velx * time_sec
		self.circle_y += self.ball_vely * time_sec

		# We need to change this parameters:
		if self.circle_x <= self.bar1_x + 10.:
			if self.circle_y >= self.bar1_y - 7.5 and self.circle_y <= self.bar1_y + 42.5:
				self.circle_x = 20.
				self.ball_velx = -self.ball_velx
		if self.circle_x >= self.bar2_x - 20.:
		       	if self.circle_y >= self.bar2_y - 7.5 and self.circle_y <= self.bar2_y + 42.5:
				self.circle_x = 600.
				self.ball_velx = -self.ball_velx
		# Until here!
		
		# If player 1 does not touch the ball:
		if self.circle_x < 0.:
			self.bar2_score += 1
			self.circle_x, self.circle_y = 400., 300.
			self.bar1_y,self.bar_2_y = 275., 275.
		# If player 2 does not touch the ball:
		elif self.circle_x > 790.:
			self.bar1_score += 1
			self.circle_x, self.circle_y = 400., 300.
			self.bar1_y, self.bar2_y = 275., 275.

		# And also this ones:
		if self.circle_y <= 10.:
			self.circle_y = 10.
			self.ball_vely = -self.ball_vely
		elif self.circle_y >= 580:
			self.circle_y = 580
			self.ball_vely = -self.ball_vely
		# Unitl here!

		# Print the background again:
		self.green.draw(self.screen)
		
		# Print the items:
		self.screen.blit(bar1,(self.bar1_x,self.bar1_y))
		self.screen.blit(bar2,(self.bar2_x,self.bar2_y))
		self.screen.blit(self.circle,(self.circle_x,self.circle_y))
		
if __name__ == '__main__':
	myGame = PhonePong()
	myGame.run()

	

















	
	
