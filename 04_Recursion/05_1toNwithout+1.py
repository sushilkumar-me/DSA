def rec(i, n): 
    if i< 1: 
        return 
    rec(i -1, n)
    print(i)

n = 3 
rec(n, n)