l = [1,2,3,4,5,3,1]
n = float("inf")
for i in range(len(l)):
    if l[i] < n:
        n = l[i]

print(n)