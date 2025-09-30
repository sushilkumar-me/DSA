a = [5,4,3,2,1]
n = len(a)
for i in range(n-1, 0, -1):
    didSwap= 0
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            didSwap=1
    print("runs")
    if didSwap == 0:
        break
print(a)