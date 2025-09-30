a =[14,9,15,12,6,8,13]
n = len(a)
for i in range(n):
    j = i 
    while j > 0 and a[j-1] > a[j]: 
        a[j-1], a[j] = a[j], a[j-1]
        j -= 1 

print(a)