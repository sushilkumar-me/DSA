def f(n, a): 
    cnt = 0 
    for i in range(len(a)):
        if a[i] == n:
            cnt += 1
    return cnt 

n = 3
a = [1,2,3,3]
print(f(n,a))
