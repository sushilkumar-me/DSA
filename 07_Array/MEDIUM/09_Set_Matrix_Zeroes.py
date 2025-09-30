def markrow(i):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            matrix[i][j] = -1 
def markcol(j):
    for i in range(len(matrix)):
        if matrix[i][j] != 0:
            matrix[i][j] = -1 

def brute(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                markrow(i)
                markcol(j)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0 
    return matrix

def brute2(matrix):
    n = [0]*len(matrix)
    m = [0]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                n[i] = 1 
                m[j] = 1 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if n[i] == 1 or m[j] == 1:
                matrix[i][j] = 0
    return matrix

def better(matrix):
    s1 = set() 
    s2 = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                s1.add(i)
                s2.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in s1 or j in s2: 
                matrix[i][j] = 0 

    return matrix 
def optimal(matrix):
    col0 = 1 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if matrix[i][j] == 0:
                matrix[i][0] = 0 
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0   
    
    for i in range(1,len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] != 0 :
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0
    if col0 == 0: 
        for i in range(len(matrix)):
            matrix[i][0] = 0
    return matrix

            
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(optimal(matrix))