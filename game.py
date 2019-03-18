import pygame
from pygame.locals import *
import glob
from maze import *
from material import *
from search import *
from AStar import *

class Game:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1000,1000), 0, 32)
    self.fpsClock = pygame.time.Clock()
    self.map = Maze()
    self.pacman_img = None
    self.monster_img = None
    self.food_img = None
    self.loadImage()

  def loadImage(self):
    self.pacman_img = pygame.image.load('pacman.png')
    self.pacman_img = pygame.transform.scale(self.pacman_img, (square_width, square_height))
    self.monster_img = pygame.image.load('monster.png')
    self.monster_img = pygame.transform.scale(self.monster_img, (23, 23))
    self.food_img = pygame.image.load('food.png')
    self.food_img = pygame.transform.scale(self.food_img, (24, 24))

  def drawPacman(self, x, y):
    #pygame.draw.rect(self.screen, red, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.pacman_img, (x*20, y*20, square_width, square_height))

  def drawWall(self, x, y):
    pygame.draw.rect(self.screen, green, (x*20, y*20, square_width, square_height), 2)

  def drawFood(self, x, y):
    #pygame.draw.rect(self.screen, blue, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.food_img, (x*20, y*20, square_width, square_height))

  
  def drawMonster(self, x, y):
    #pygame.draw.rect(self.screen, purple, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.monster_img, (x*20, y*20, square_width, square_height))


  def drawMap(self):
    self.screen.fill(black)
    self.map.loadMap("map1.txt")
    self.map.setPos()
    rows, cols = (self.map.N, self.map.M)
    for col in range(cols):
      for row in range(rows):
        value = self.map.matrix[row][col]
        if value == 1:
          self.drawWall(col, row)
        elif value == 2:
          self.drawFood(self.map.food[0], self.map.food[1])
        elif value == 3:
          self.drawMonster(self.map.monster[0], self.map.monster[1])

  def moveCharacter(self, code, x,y):
    self.drawMap()
    if(code == 1):
      self.drawPacman(x, y)
    pygame.display.update()
    self.fpsClock.tick(10)
  
  def play(self):
    self.drawMap()
    N = self.map.N
    M = self.map.M
    pacman = self.map.pacman
    food = self.map.food
    matrix = self.map.matrix

    s = Search(AStar())
    path = s.search(pacman, food, matrix)
    print(path)
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          exit()
      for i in range(len(path)):
        x, y = path[i]
        self.moveCharacter(1, x, y)
      '''while(y+1 < N and matrix[y+1][x] == 0):
        y+=1
        self.moveCharacter(1,x,y)
      while(x-1 >= 0 and matrix[y][x-1] == 0):
        x-=1
        self.moveCharacter(1,x,y)
      while(y-1 >= 0 and matrix[y-1][x] == 0):
        y-=1
        self.moveCharacter(1,x,y)
      while(x+1 < M and matrix[y][x+1] == 0):
        x+=1
        self.moveCharacter(1,x,y)'''