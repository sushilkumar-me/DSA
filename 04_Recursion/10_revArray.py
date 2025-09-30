def f(i, a, n): 
    if i >= n/2: 
        return 
    a[i], a[n-i-1] = a[n-i-1], a[i]
    f(i +1, a, n)

n = 5 
a = [1, 2, 3, 4, 5]
f(0, a, n)
print(a) 

