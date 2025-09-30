from math import sqrt
def divisors(n):
    r = []
    j = int(sqrt(n))
    for i in range(1, j+1): # we can take i*i+1 as condition
        if n % i == 0:
            r.append(i)
            
            if n/i != i: 
                r.append(n //i)
    r.sort()
    for i in r:
        print(i, end=' ')

divisors(36)