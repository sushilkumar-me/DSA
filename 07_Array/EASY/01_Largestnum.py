l = [16,17,4,23]
n = l[0]
for i in range(1,len(l)):
    if l[i]> n:
        n = l[i]
print(n)