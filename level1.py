def input():
    fi = open("map1.txt",'r')
    N, M = [int(i) for i in fi.readline().split()]
    matrix = [[int(j) for j in line.split()] for line in fi]
    x,y = matrix[-1][:]
    matrix.pop(-1)
    pre = []
    end = []
    r = BFS(pre,tuple([x,y]),end,matrix,M,N)
    return 0

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

def bfsInner(start,end,map,m,n): 
    pre = {}
    q = [start] 
    current = 0
    mark = [[0] * m for i in range(n)]
    while len(q) > 0:
        current = q.pop()  
        _successors = successors(current[0],current[1]) 
        if destination_check(map,current):
            end.append(tuple(current))     
            return pre
        for node in _successors: 
            if valid(node,map,m,n) and mark[node[0]][node[1]] == 0: 
                q.insert(0,node) 
                mark[node[0]][node[1]] = 1
                pre[node] = current
                if destination_check(map,current):
                    end.append(tuple(current)) 
                    print (pre)
                    return pre
    return 0

def intepret(pre,start,end):  
    if pre == 0:
        return 0
    path = [] 
    cur = pre[end[0]]
    while cur[0] != start[0] or cur[1] != start[1] : 
        path.insert(0,cur)
        cur = pre[cur]
    path.insert(0,start)
    print(path)
    return path 

def BFS(pre,start,end,map,m,n): 
    end = []
    pre = bfsInner(start,end,map,m,n)
    return intepret(pre,start,end)



input()