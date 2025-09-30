def brute_solution(arr):
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if i%2 == 0:
                if arr[i] < 0:
                    if arr[j] >= 0:
                        arr[i], arr[j] = arr[j], arr[i]
            if i%2 != 0:
                if arr[i] >= 0:
                    if arr[j] < 0:
                        arr[i], arr[j] = arr[j], arr[i]
    return arr
def brute_solution2(arr):
    pos = []
    neg = [] 
    n = len(arr)
    for i in range(n):
        if arr[i] >= 0 :
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(0,n//2,1):
        arr[i*2] = pos[i]
        arr[i*2+1] = neg[i]
    return arr
def better_solution(arr):
    pos = 0 
    neg = 1 
    result = [0]* len(arr)
    for i in range(len(arr)):
        if arr[i] >=0:
            result[pos] = arr[i]
            pos += 2
        elif arr[i] < 0:
            result[neg] = arr[i]
            neg += 2
    return result
                

arr = [3,1,-2,-5,2,-4]
#print(brute_solution2(arr))
print(better_solution(arr))
