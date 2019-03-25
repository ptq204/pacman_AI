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

def stimulate_bot(map,pacman,ghost,m,n): 
    current_h = [[mahattanDistance(g[0],g[1],pacman[0],pacman[1])] for g in ghost]
    for g in ghost:                

def AdversialSearch(map,start,h,m,n): 
    pass 