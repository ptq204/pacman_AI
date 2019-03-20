from Level1 import *

input()

def Heuristic(map,nodes,m,n): 
    res = [0]*len(nodes)
    for i in range(0,n):  
        if not valid(nodes[i],map,m,n):
            res[i] = -1 
        elif nodes[i] == 2:
            res[i] = 3 
        else:
            res[i] = 0
    return res 

def search(start,end,map,m,n): 
    q = [start]
    h = [0]
    current = 0
    path = []
    mark = [[0] * m for i in range(n)]
    count = 0; 
    while q > 0 and count <= m*n: 
        current = q.pop()
        if (mark[current[0]][current[1]] == 0):
            mark[current[0]][current[1]] == 1
            count+=1
        h.pop()  
        adjacent = successors(current[0],current[1]) 
        heuristic = Heuristic(map,adjacent,m,n) 
        next = 0 
        for i in range(0,4): 
            heuristic[i] -= mark[adjacent[i][0]][adjacent[i][1]]
            if heuristic[next] < heuristic[i]:
                next = i
        path.append(adjacent[next])
        q.append(adjacent[next])
    return path

input()