def successors(int i,int j): 
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    res = []
    for i in range(0,4)
        res.append((i+dx,j+dy))
    return res


def AssignHeuristic(i,j,value,h)
    if h[i][j] < value:
        h[i][j] = value 
    pass

def search(known_map,start,end): 
    q = [start] 
    #the higher value in known_map the least 
    current = 0
    while len(q) > 0: 
        current = q.pop() 
        adjacent = successors()
