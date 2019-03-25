
def input():
    fi = open("map.txt",'r')
    N, M = [int(i) for i in fi.readline().split()]
    matrix = [[int(j) for j in line.split()] for line in fi]
    x,y = matrix[-1][:]
    matrix.pop(-1)
    pre = []
    end = []
    r = BFS(matrix,tuple([x,y]),M,N)
    print r 
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
                

def advancedBFS(map,start,ref_end,m,n): 
    q = [start]
    pre = {}
    pre[start] = -1
    while len(q) > 0: 
        cur = q.pop() 
        if destination_check(map,cur): 
            ref_end = cur
            return pre 
        adjacent = SortedSuccessor(map, cur,m,n) 
        for node in adjacent: 
            q.insert(0,node)
            pre[node] = cur
            if destination_check(map,node): 
                ref_end = node
                return pre


def BFS(map,start,m,n):
    end = 0 
    pre = advancedBFS(map,start,end,m,n)
    if len(pre) > 1: 
        path = []
        cur = end 
        while cur != -1: 
            path.insert(0,cur)
            cur = pre[cur]
        return path
    return 0 

input()