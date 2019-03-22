import sys
from util import *

class AStar():

  def __init__(self):
    pass
  
  def heuristic(self, current, destination):
    # Mahathan distance
    return abs(current[0] - destination[0]) + abs(current[1] - destination[1])  

  def search(self, source, destination, matrix):
    cost = {}
    isVisited = {}
    prev = {}
    h = {}

    cost[source] = 0
    isVisited[source] = True
    current = source

    h[current] = self.heuristic(current, destination)

    while(not equal(current, destination)):
      
      # Find all paths from current node to its childs
      for i in range(4):
        x, y = current
        if(i == 0): x += 1
        elif(i == 1): x -= 1
        elif(i == 2): y += 1
        else: y -= 1
        tmp = matrix[x][y]
        h[(x,y)] = self.heuristic((x,y), destination)

        if(tmp == 0 or tmp == 2):
          new_cost = cost[current] + tmp + h[(x,y)] if(current == source) else cost[current] + tmp - h[current] + h[(x,y)]
          if(not cost.__contains__((x, y)) or new_cost < cost[(x,y)]):
            prev[(x,y)] = current
            cost[(x,y)] = new_cost
      
      # Find child node with minimum path cost
      min_cost = sys.maxsize
      min_index = current
      for j in cost.keys():
        if(not isVisited.__contains__(j) and cost[j] < min_cost):
          min_cost = cost[j]
          min_index = j
      
      if(equal(min_index, current)):
        break
      current = min_index
      isVisited[current] = 1
      if(equal(current, destination)):
        path = printPath(source, destination, prev)
        return path
