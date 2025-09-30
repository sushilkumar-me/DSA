from math import sqrt
def primecheck(n): 
    c = 0
    for i in range(1, int(sqrt(n))+1, 1): 
        if n% i == 0:
            c +=1
            if n//i != i: 
                c += 1
            
    if c == 2: 
        return True 
    else: 
        return False

print(primecheck(1))
