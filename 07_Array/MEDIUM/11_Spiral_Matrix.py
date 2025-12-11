def sm(matrix):
    left = 0 
    right = len(matrix[0]) -1 
    top = 0 
    bottom = len(matrix)-1
    l = [] 
    while left <= right and top <= bottom:
        # 1. Traverse Right (Top Row) 
        for i in range(left,right+1):
            l.append(matrix[top][i])
        top += 1
        # 2. Traverse Down (Right Column)
        if top <= bottom:
            for i in range(top, bottom+1):
                l.append(matrix[i][right] )
            right -= 1 
        # 3. Traverse Left (Bottom Row)
        if top <= bottom and left <= right:
            for i in range(right, left-1,-1):
                l.append(matrix[bottom][i])
            bottom -= 1
        # 4. Traverse Up (Left Column)
        if top <= bottom and left <= right:
            for i in range(bottom, top-1,-1):
                l.append(matrix[i][left])
            left += 1       
    return l

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sm(matrix))