l = [3,2,6,1]
n = float("inf")
sn = float("inf")

for i in range(len(l)):
    if l[i] < n:
        sn = n
        n = l[i]
print(sn)