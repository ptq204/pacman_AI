def drawMap(filename,m,n): 
    fo = open(filename,'w')
    fo.write(str(m) + ' ' + str(n) + '\n') 
    for i in range(0,m):
        for j in range(0,n): 
            fo.write('1 ') 
        fo.write('\n')
    fo.close() 

drawMap('map30.txt',30,30)