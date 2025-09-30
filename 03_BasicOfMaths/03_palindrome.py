def palidrome(n): 
    dup = n 
    rev = 0 
    while n > 0: 
        lastdigit = n %10 
        rev = rev * 10 + lastdigit
        n = n // 10
    if dup == rev: 
        return True
    else:  
        return False
    
print(palidrome(121))