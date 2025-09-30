l = [13,46,24,52,20,9]

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            min = j
        else:
            min = i
    l[min], l[i] = l[i], l[min]

print(l)





