n = input()
l = ['a','a','b','c','c','c']
hash = [0]*256
for i in range(len(l)):
    hash[ord(l[i])] += 1
print(hash[ord(n)])
