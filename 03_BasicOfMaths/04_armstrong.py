def armstrong(n):
    d  = n
    r = 0 
    c = 0
    while n > 0:
        n = n // 10
        c +=1
    n = d
    
    while n > 0 : 
        lastdigit = n % 10 
        r = r + lastdigit ** c
        n = n // 10
    if r == d:
        return True 
    else:
        return False

print(armstrong(1634))
