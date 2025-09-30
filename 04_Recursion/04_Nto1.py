def rec(i, n): 
    if i < 1: 
        return 
    print(i)
    rec(i -1, n)

n = 4
rec(n, n)