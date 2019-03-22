
class Maze:

  def __init__(self):
    self.matrix = None
    self.N = None
    self.M = None
    self.pacman = None
    self.monster = None
    self.food = None

  def loadMap(self, filepath):
    f = open(filepath)
    self.N, self.M = [int(i) for i in f.readline().split()]
    self.matrix = [[int(j) for j in line.split()] for line in f]
    i,j = self.matrix[-1][:]
    self.pacman = (i,j)
    self.matrix.pop(-1)
    f.close()

  def setPos(self):
    for i in range(self.N):
      for j in range(self.M):
        if(self.matrix[i][j] == 3):
          self.monster = (i,j)
        elif(self.matrix[i][j] == 2):
          self.food = (i,j)