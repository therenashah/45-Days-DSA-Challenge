matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
m = len(matrix)
n = len(matrix[0])
rowNumbers = []
colNumbers = []
for i in range(0,m):
    for j in range(0,n):
        if matrix[i][j] == 0:
                    rowNumbers.append(i)
                    colNumbers.append(j)
for x in rowNumbers:
    for j in range(0,n):
          matrix[x][j] = 0
for i in range(0,m):
    for y in colNumbers:
          matrix[i][y] = 0

print(matrix)

        
