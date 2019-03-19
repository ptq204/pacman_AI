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
            return pre
        for node in _successors: 
            if valid(node,map,m,n) and mark[node[0]][node[1]] == 0: 
                q.insert(0,node) 
                mark[node[0]][node[1]] == 1
                pre[node] = current
                if destination_check(map,current):
                    return pre
    return 0

def BFS(start,end,map,m,n): 
    pre = bfs(start,end,map,m,n)
    if pre == 0:
        return 0
    path = [] 
    cur = pre[end]
    while cur in pre.keys(): 
        path.append(cur)
        cur = pre[cur]
    return path 