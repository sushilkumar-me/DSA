def check(i, n, s): 
    if s[i] != s[n-i-1]:
        return False
    if i >= n/2:
        return True
    return check(i + 1, n, s)

s= "madm"
n = len(s)
print(check(0, n, s))
     