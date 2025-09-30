n = int(input())
a = [1,2,1,3,2]
hash = [0]*10**9
for i in range(len(a)):
    hash[a[i]] += 1

print(hash[n])
