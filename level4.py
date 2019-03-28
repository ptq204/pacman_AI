from level1 import successors
from level3 import successors_HillClimbing


def mahattanDistance(x,y,z,t,):
    return abs(x-z) + abs(y-t) 

def HeuristicLv4(gameMap,m,n): 
    foods = [] 
    h = [[m*n] * m for i in range(n)]
    for i in range(0,m):
        for j in range(0,n): 
            if gameMap[i][j] == 2: 
                foods.append((i,j))
    for food in foods:
        for i in range(0,m):
            for j in range(0,n): 
                d = mahattanDistance(i,j,food[0],food[1])
                if h[i][j] > d:
                    h[i][j] = d
    return h

def bound_check(x,y,m,n):
    if x < 0 or y < 0:
        return False
    if x >= n or y >= m:
        return False 
    return True

def valid(i,j,m,n,gameMap,ghosts): 
    if not bound_check(i,j,m,n):
        return False
    if gameMap[i][j] == 1:
        return False
    for g in ghosts:
        if mahattanDistance(g[0],g[1],i,j) <= 1:
            return False 
    return True

def stimulate_bot(gameMap,pacman,ghosts,m,n,h_pacman): 
    res = [] 
    for g in ghosts: 
        adj = successors(g[0],g[1]) 
        h = adj[0]
        a = m*n*n 
        for move in adj: 
            if bound_check(move[0],move[1],m,n) and gameMap[move[0]][move[1]] != 1:
                if a > mahattanDistance(move[0],move[1],pacman[0],pacman[1]):
                    a = mahattanDistance(move[0],move[1],pacman[0],pacman[1]) 
                    h = move
                elif a == mahattanDistance(move[0],move[1],pacman[0],pacman[1]) and h_pacman[move[0]][move[1]] < h_pacman[h[0]][h[1]]: 
                    a = mahattanDistance(move[0],move[1],pacman[0],pacman[1]) 
                    h = move
        res.append(h) 
    return res 
'''    
Pacman:                   x
                    /   /   \   \            
Pacman:            1   2    3     4 

Pacman:   11 12 13 14  21 22 23 24   31 32 33 34  41 42 43 44 '''
def PacMan_Choose(possibleMoves,h,gameMap,m,n,ghosts):
    res = 0  
    best_h = m*n*n
    for move in possibleMoves:
        if valid(move[0],move[1],m,n,gameMap,ghosts):
            if best_h > h[move[0]][move[1]]: 
                best_h = h[move[0]][move[1]]
                res = move
    return res 

def startGame(gameMap,pacman,m,n):
    h = HeuristicLv4(gameMap,m,n)
    blankgameMap =[row[:] for row in gameMap]
    path = [pacman] 
    start_ghosts = []
    for i in range(0,m):
        for j in range(0,n): 
            if blankgameMap[i][j] == 3: 
                start_ghosts.append(tuple([i,j])) 
                blankgameMap[i][j] = 0 
    ghosts = [start_ghosts]
    while True: 
        possibleMoves = successors_HillClimbing(gameMap,pacman[0],pacman[1],m,n) 
        nextMove = PacMan_Choose(possibleMoves,h,blankgameMap,m,n,ghosts[-1])
        if nextMove != 0: 
            path.append(nextMove) 
        else:
            break 
        ghostMoves = stimulate_bot(blankgameMap,pacman,ghosts[-1],m,n,h) 
        ghosts.append(ghostMoves)
    return path,ghosts 
def inputgameMap():
    fi = open("map30.txt",'r')
    N, M = [int(i) for i in fi.readline().split()]
    matrix = [[int(j) for j in line.split()] for line in fi]
    x,y = matrix[-1][:]
    matrix.pop(-1)
    startGame(matrix,(x,y),M,N)
  
#     print(r) 
#     # '''There is a graph with n nodes and
#     #         There is no loop, no cycle
#     #         There is at most one edge between a pair of vertex 
#     #         if there are exactly 2 nodes '''
    
inputgameMap() 