def rec(i): 
    if i== 0: 
        return 
    rec(i -1)
    print(i, end=" ")

n = 3 
rec(n)