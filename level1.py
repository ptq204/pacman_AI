def input() 
    fi = open("map1.txt",'r')
    N, M = [int(i) for i in f.readline().split()]
	matrix = [[int(j) for j in line.split()] for line in f]
	x,y = matrix[-1][:]
	matrix.pop(-1)
    pre = []
    end = (0,0)
    r = BFS(pre,(x,y),matrix,end,M,N)

def successors(int i,int j): 
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    res = []
    for i in range(0,4)
        res.append((i+dx,j+dy))
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
    return (map[node[0]][node[1]] == 0) 

def destination_check(map,node): 
    return map[node[0]][node[1]] == 2

def bfsInner(start,end,map,m,n): 
    pre = {}
    q = [start] 
    current = 0
    mark = [[0]*m]*n
    while len(q) > 0:
        current = q.pop()  
        _successors = successors(current[0],current[1]) 
        if destination_check(map,current):
            end = current
            return pre
        for node in _successors: 
            if valid(node,map,m,n) and mark[node[0]][node[1]] == 0: 
                q.insert(0,node) 
                mark[node[0]][node[1]] == 1
                pre[node] = current
                if destination_check(map,current):
                    end = current
                    return pre
    return 0

def BFS(pre,start,end,map,m,n): 
    pre = bfs(Inner(start,end,map,m,n)
    return intepret(pre)

def intepret(pre):  
    if pre == 0:
        return 0
    path = [] 
    cur = pre[end]
    while cur in pre.keys(): 
        path.append(cur)
        cur = pre[cur]
    return path 

def dfs(start,end,map,m,n, limit): 
    pre = {}
    q = [start] 
    current = 0
    mark = [[0]*m]*n
    lim = 0
    while len(q) > 0 and lim < limit:
        current = q.pop()  
        lim+=1
        _successors = successors(current[0],current[1]) 
        if destination_check(map,current):
            return pre
        for i in range(len(_successors-1),0,-1): 
            node = _successors[i]
            if valid(node,map,m,n) and mark[node[0]][node[1]] == 0: 
                q.append(node) 
                mark[node[0]][node[1]] == 1
                pre[node] = current
                if destination_check(map,current):
                    return pre
    return 0

def IDS(start,end,map,m,n): 
    for i in range(3,m*n+1): 
        pre = dfs(start,end,map,m,n)
        if pre != 0:
            return intepret(pre)
    return 0 

input()