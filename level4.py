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

def validForGhost(node,gameMap,m,n): 
    if not bound_check(node[0],node[1],m,n):
        return False
    if gameMap[node[0]][node[1]] == 1:
        return False 
    return True 

def stimulate_bot(gameMap,pacman,ghosts,m,n,h_pacman): 
    res = [] 
    for g in ghosts: 
        adj = successors(g[0],g[1]) 
        h = g
        a = m*n*n 
        for move in adj: 
            if validForGhost(move,gameMap,m,n):
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
def PacMan_Choose(possibleMoves,h,gameMap,turnMatrix, current_turn, m,n,ghosts):
    res = 0  
    best_h = m*n*n
    for move in possibleMoves:
        if valid(move[0],move[1],m,n,gameMap,ghosts) and current_turn - turnMatrix[move[0]][move[1]] > 1:
            if best_h > h[move[0]][move[1]]: 
                best_h = h[move[0]][move[1]]
                res = move
    return res 

def TryBFS(gameMap,h,ghosts,pacman,m,n): 
    q = [tuple(pacman)] 
    pre = {} 
    pre[tuple(pacman)] = -1 
    end = 0 
    mark = [[False] * m for i in range(n)]
    mark[pacman[0]][pacman[1]] = True 
    stillNotFound = True
    while len(q) > 0 and stillNotFound: 
        cur = q.pop() 
        if gameMap[cur[0]][cur[1]] == 2: 
            end = cur 
            stillNotFound = False
            break 
        mark[cur[0]][cur[1]] = True 
        adjacent1 = successors_HillClimbing(gameMap, cur[0],cur[1],m,n)
        adjacent = [] 
        for node in adjacent1: 
            if validForGhost(node,gameMap,m,n): 
                k = 0 
                while k < len(adjacent) and h[node[0]][node[1]] < h[adjacent[k][0]][adjacent[k][1]]: 
                    k +=1 
                adjacent.insert(k,tuple(node))
        for node in adjacent:
            if not mark[node[0]][node[1]]: 
                q.insert(0,node)
                pre[tuple(node)] = cur
                mark[node[0]][node[1]] = True 
                if gameMap[cur[0]][cur[1]] == 2: 
                    end = cur
                    q.clear() 
                    stillNotFound = False
                    break
                    
    if end != 0: 
        respath = [end]
        cur = end 
        while cur != -1: 
            respath.insert(0,cur)
            cur = pre[tuple(cur)]
        # if respath[-1][0] == pacman[0] and respath[-1][1] == pacman[1]:
        #     return 0 
        respath.remove(respath[0])
        return respath
    return 0


def PacManBFS(pacman,gameMap,h,m,n,ghosts,moveQueue): 
    if len(moveQueue) : 
        cur = moveQueue[0]
        if valid(cur[0],cur[1],m,n,gameMap,ghosts):
            moveQueue.remove(cur)
            return cur
        else: 
            newPath,end = TryBFS(gameMap,ghosts,pacman,m,n) 
            if newPath != 0: 
                moveQueue.clear() 
                moveQueue.append(newPath)
                cur = moveQueue[0]
                moveQueue.remove(cur)
                return cur 
    else: #run GBFS to find the path and add it to queue 
        newPath = TryBFS(gameMap,h,ghosts,pacman,m,n) 
        if newPath != 0: 
            moveQueue.clear() 
            moveQueue[:] = newPath[:]
            cur = moveQueue[0]
            moveQueue.remove(cur)
            return cur 
    return 0 



def startGame(gameMap,pacman,m,n):
    h = HeuristicLv4(gameMap,m,n)
    blankgameMap =[row[:] for row in gameMap]
    path = [pacman] 
    start_ghosts = []
    turnMatrix = [[0]*m for i in range(n)]
    turnMatrix[pacman[0]][pacman[1]] = 1
    tempq = [] 
    for i in range(0,m):
        for j in range(0,n): 
            if blankgameMap[i][j] == 3: 
                start_ghosts.append(tuple([i,j])) 
                blankgameMap[i][j] = 0 
    ghosts = [start_ghosts]
    current_turn = 1 
    moveQueue = []
    while True: 
        possibleMoves = successors_HillClimbing(gameMap,path[-1][0],path[-1][1],m,n) 
        # nextMove = PacMan_Choose(possibleMoves,h,blankgameMap,m,n,turnMatrix,current_turn,ghosts[-1])
        current_turn +=1 
        nextMove = PacManBFS(path[-1],gameMap,h,m,n,ghosts[-1],moveQueue)
        if nextMove != 0: 
            path.append(nextMove) 
            # turnMatrix[nextMove[0]][nextMove[1]] = current_turn
        else:
            break 
        ghostMoves = stimulate_bot(blankgameMap,pacman,ghosts[-1],m,n,h) 
        ghosts.append(ghostMoves)
    return path,ghosts 
def inputgameMap():
    fi = open("map40.txt",'r')
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