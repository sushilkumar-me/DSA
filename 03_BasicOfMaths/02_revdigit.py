def rev(n):
    rev = 0 
    while n > 0: 
        lastdigit = n%10 
        rev = rev *10 + lastdigit
        n = n // 10
    return rev

print(rev(123))