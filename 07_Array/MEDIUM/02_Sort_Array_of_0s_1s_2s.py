
## Better 
def better_solution(arr):
    cnt0,cnt1,cnt2= 0,0,0
    for i in arr:
        if i == 0:
            cnt0 += 1
        elif i == 1:
            cnt1 += 1
        elif i == 2:
            cnt2 += 1
    for i in range(cnt0):
        arr[i] = 0
    for i in range(cnt0,cnt0+cnt1):
        arr[i] = 1
    for i in range(cnt0+cnt1,len(arr)):
        arr[i] = 2
    return arr

## OPTIMAL SOLUTION (DEATCH NATIONAL FLAG ALGORITHM)
def optimal_solution(arr):
    low = 0
    mid = 0 
    high = len(arr)-1
    for i in range(len(arr)):
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid +=1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            mid +=1
            high -= 1
        return arr

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
print(better_solution(arr))
print(optimal_solution(arr))