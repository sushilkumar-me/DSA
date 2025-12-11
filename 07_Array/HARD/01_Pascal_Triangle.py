def Pascal_Triangle(n): 
    l = [] 
    l.append([1]) 
    if n == 1: 
        return l
    for i in range(1,n): 
        prevRow = l[i-1]
        r = [] 
        r.append(1) 
        for j in range(i-1): 
            r.append(prevRow[j]+prevRow[j+1])
        r.append(1)
        l.append(r)
    return l 

print(Pascal_Triangle(3))