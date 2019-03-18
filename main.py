from game import *

def AStar():
  cost = [sys.maxsize]*N
  isVisited = [False]*N
  prev = [0]*N
  queue = []

  cost[source] = 0
  isVisited[source] = True
  current = source
  queue.append(source)
  f.write('{}'.format(current))

  while(current != destination):
    
    # Find all paths from current node to its childs
    for i in range(N):
      tmp = matrix[current][i]
      if(tmp > 0):
        new_cost = cost[current] + tmp + h[i] if(current == source) else cost[current] + tmp - h[current] + h[i]
        if(new_cost < cost[i]):
          prev[i] = current
          cost[i] = new_cost
    
    # Find child node with minimum path cost
    min_cost = sys.maxsize
    min_index = current
    for j in range(len(cost)):
      if(isVisited[j] == 0 and cost[j] < min_cost):
        min_cost = cost[j]
        min_index = j
    
    if(min_index == current):
      break
    current = min_index
    isVisited[current] = 1
    if(current == destination):
      return

if __name__ == "__main__":
	g = Game()
	g.play()
		
		
