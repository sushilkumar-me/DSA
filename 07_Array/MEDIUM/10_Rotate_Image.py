def brute(matrix):
    r = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            r[j][len(matrix)-1-i] = matrix[i][j] 
    return r 
def better(matrix):
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    
    for i in range(len(matrix)):
        b = len(matrix)-1
        for j in range(len(matrix[i])//2):
            matrix[i][j], matrix[i][b] = matrix[i][b], matrix[i][j]
            b -=1
    

    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(better(matrix))