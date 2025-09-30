l = [0,1,3]
missing = len(l)
for i,num, in enumerate(l):
    print(missing, i, num)
    missing ^= i^ num 
print(missing) 