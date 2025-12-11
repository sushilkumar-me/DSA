arr =[1,1,1,2,3,4]

j=0
for i in range(1,len(arr)):
    if arr[i] != arr[j]:
        j +=1
        arr[j] = arr[i]

print(i,arr[:j+1])
