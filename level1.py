def successors(int i,int j): 
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    res = list() 
    for i in range(0,4)
        res.append([i+dx,j+dy]) 
    return res

def valid(node,map,m,n):
    x = node[0]
    y = node[1]
    if x < 0 or y < 0:
        return False
    if x >= n or y >= m:
        return False 
    return (map[node[0]][node[1]] == 0) 

def bfs(start,end,map,m,n): 
    pre = {}
    q = [start] 
    current = 0
    while len(q) > 0:
        current = q.pop()  
        _successors = successors(current[0],current[1]) 
        if current == end:
            return pre
        for node in _successors: 
            if valid(node,map,m,n): 
                q.insert(0,node) 
                pre[node] = current
                if node == end:
                    return pre