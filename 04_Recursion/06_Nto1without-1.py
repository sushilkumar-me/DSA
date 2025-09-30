def rec(i, n): 
    if i > n: 
        return 
    rec(i+ 1, n)
    print(i)
n = 3 
rec(1, n)