def count(n): 
    c = 0
    while n > 0: 
        n = n // 10
        c += 1
    return c 

n = 1234
print(count(n))
