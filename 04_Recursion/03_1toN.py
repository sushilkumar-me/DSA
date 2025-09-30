def rec(i, n): 
    if i > n:
        return 
    print(i)
    rec(i +1, n)

n = 2
rec(1, n)