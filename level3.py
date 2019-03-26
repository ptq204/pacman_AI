def successors( i, j): 
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    res = []
    for k in range(0,4):
        res.append(tuple([i+dx[k],j+dy[k]]))
    return res


def valid(node,map,m,n):
    x = node[0]
    y = node[1]
    if x < 0 or y < 0:
        return False
    if x >= n or y >= m:
        return False 
    if map[node[0]][node[1]] == 2:
        return True
    if map[node[0]][node[1]] == 0: 
        return True
    return False

def destination_check(map,node): 
    if map[node[0]][node[1]] == 2:
        return True
    return False

def SortedSuccessor(map,node,m,n): 
    r = successors(node[0],node[1])
    res = []
    for cur in r: 
        if valid(cur,map,m,n): 
            k = 0
            while k < len(res) and map[res[k][0]][res[k][1]] > map[cur[0]][cur[1]]: 
                k+=1 
            res.insert(k,cur)
    return res 



def best_successor(map,node, m,n,mark):
    adj = successors(node[0],node[1])

    r = []
    for node in adj: 
        if valid(node,map,m,n) and not  mark[node[0]][node[1]]: 
            if map[node[0]][node[1]] == 2: 
                return node
            r.append(node)
    if len(r) > 0:
        return r[0]
    return 0

def hill_climbing(map,start,m,n):
    path = [start]
    mark = [[False] * m for i in range(n)]
    mark[start[0]][start[1]] = True
    while True: 
        nextMove = best_successor(map,path[-1],m,n,mark) 
        if nextMove!= 0: 
            path.append(nextMove)
            mark[nextMove[0]][nextMove[1]] = True 
        else: break
    return path