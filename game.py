import pygame
from pygame.locals import *
import glob
from maze import *
from material import *
from search import *
from AStar import *
from level1 import *
from level3 import *
class Game:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((700,700), 0, 32)
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

  def drawPacman(self, i, j):
    #pygame.draw.rect(self.screen, red, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.pacman_img, (j*20, i*20, square_width, square_height))

  def drawWall(self, i, j):
    pygame.draw.rect(self.screen, purple, (j*20, i*20, square_width, square_height), 2)

  def drawFood(self, i, j):
    #pygame.draw.rect(self.screen, blue, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.food_img, (j*20, i*20, square_width, square_height))

  
  def drawMonster(self, i, j):
    #pygame.draw.rect(self.screen, purple, (x*20, y*20, square_width, square_height), 0)
    self.screen.blit(self.monster_img, (j*20, i*20, square_width, square_height))


  def drawMap(self, level):
    self.screen.fill(black)
    filename = ''
    if(level == 1):
      filename = 'level1_0.txt'
    elif(level == 2):
      filename = 'level2_2.txt'
    elif(level == 3):
      filename = 'level2_1.txt'
    
    self.map.loadMap(filename)
    self.map.setPos()
    rows, cols = (self.map.N, self.map.M)
    for row in range(rows):
      for col in range(cols):
        value = self.map.matrix[row][col]
        if value == 1:
          self.drawWall(row, col)
        elif value == 2:
          self.drawFood(row, col)
        elif value == 3:
          self.drawMonster(row, col)

  def moveCharacter(self, code, s, d):
    self.erase(s[0], s[1])
    if(code == 1):
      self.drawPacman(d[0], d[1])
    if(code == 2):
      self.drawMonster(d[0], d[1])
    pygame.display.update()
    self.fpsClock.tick(12)
  
  def erase(self, i, j):
    pygame.draw.rect(self.screen, black, (j*20, i*20, square_width, square_height))
  
  def play(self):
    level = int(input("Choose level: "))

    self.drawMap(level)

    N = self.map.N
    M = self.map.M
    pacman = self.map.pacman
    food = self.map.food
    matrix = self.map.matrix
    score = 0
    path = None

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          exit()

      if(level == 1 or level == 2):
        path = BFS([],self.map.pacman, [], matrix, M, N)
        print(path)
        if(path != None):
          path.append(self.map.food)
          for i in range(len(path)):
            if(i == 0):
              s = path[0]
              d = path[0]
            else:
              s = path[i-1]
              d = path[i]
            self.moveCharacter(1, s, d)
            score -= 1
          self.erase(path[-1][0], path[-1][1])
          self.drawFood(path[-1][0], path[-1][1])
          score += 10

      elif(level == 3):
        path = search(self.map.pacman, [], matrix, M, N)
      print('score: {}'.format(score))