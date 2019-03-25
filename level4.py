from level1 import successors,valid


def mahattanDistance(x,y,z,t,):
    return abs(x-z) + abs(y-t) 

def HeuristicLv4(map,nodes,m,n): 
    foods = [] 
    h = [[m*n] * m for i in range(n)]
    for i in range(0,m):
        for j in range(0,n): 
            if map[i][j] == 2: 
                foods.append((i,j))
    for food in foods:
        for i in range(0,m):
            for j in range(0,n): 
                d = mahattanDistance(i,j,food[0],food[1])
                if h[i][j] > d:
                    h[i][j] = d
    return h

def bound_check(x,y):
    if x < 0 or y < 0:
        return False
    if x >= n or y >= m:
        return False 
    return True
def stimulate_bot(map,pacman,ghosts,m,n,h_pacman): 
    res = [] 
    for g in ghosts: 
        adj = successors(g[0],g[1]) 
        h = 0 
        a = m*n  
        for n in adj: 
            if bound_check(n[0],n[1]):
                if a > mahattanDistance(n[0],n[1],pacman[0],pacman[1]):
                    a = mahattanDistance(n[0],n[1],pacman[0],pacman[1]) 
                    h = n
                elif a == mamahattanDistance(n[0],n[1],pacman[0],pacman[1]) and h_pacman[n[0]][n[1]]  
        map[]
        res.append(h) 
    return res 
'''    
Pacman:                   x
                    /   /   \   \            
Pacman:            1   2    3     4 

Pacman:   11 12 13 14  21 22 23 24   31 32 33 34  41 42 43 44 '''
def PacMan_Choose(possibleMoves,h,map,m,n):
    res = possibleMoves[0] 
    max_h = h[res[0]][res[1]]
    for m in possibleMoves:
        if max_h < h[m[0]][m[1]] and valid(m,map,m,n):
            max_h = h 
            res = m
    return res,max_h 

def Ghost_Choose(pacman,ghosts, map,h): 
    
    for g in ghosts: 
        if mahattanDistance(g[0],g[1],pa)


# Bot will choose things that minimize pacman's score
def Bot_LV1(map,pacman,ghost,m,n): 
    adj = successors()
    res = 