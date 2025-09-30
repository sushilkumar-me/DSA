def rec(n):
    global c 
    if c == 4: 
        return 
    print(c)
    c += 1
    rec(n)
c = 0 
rec(10)