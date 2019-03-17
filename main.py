import pygame
from pygame.locals import *
from numpy import loadtxt
import glob

file_path = glob.glob("./input.txt")

N = 0
M = 0
matrix = [[]]
x = -1
y = -1

screen = None


def readFileIntoMatrix(file_path):
	global N, M, matrix, x, y
	f = open(file_path)
	N, M = [int(i) for i in f.readline().split()]
	matrix = [[int(j) for j in line.split()] for line in f]
	x,y = matrix[-1][:]
	matrix.pop(-1)

def initMap():
	pygame.init()
	global screen, fpsClock
	fpsClock = pygame.time.Clock()
	screen = pygame.display.set_mode((320,320), 0, 32)
	readFileIntoMatrix("map.txt")

def drawMap():
	
	rows, cols = N,M
	for col in range(cols):
		for row in range(rows):
			value = matrix[row][col]
			if value == 1:
				pygame.draw.rect(screen, (0, 255, 0), (col*20, row*20, 20, 20), 2)
	pygame.draw.rect(screen, (255, 0, 0), (x*20, y*20, 20, 20), 0)

def move(x, y):
	screen.fill((0,0,0))
	drawMap()
	pygame.draw.rect(screen, (255, 0, 0), (x*20, y*20, 20, 20), 0)
	pygame.display.update()
	fpsClock.tick(10)

def search():
	pass

if __name__ == "__main__":
	initMap()
	drawMap()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		while(matrix[x][y+1] == 0):
			y+=1
			move(x,y)
		while(matrix[x-1][y] == 0):
			x-=1
			move(x,y)
		while(matrix[x][y-1] == 0):
			y-=1
			move(x,y)
		while(matrix[x+1][y] == 0):
			x+=1
			move(x,y)
		
