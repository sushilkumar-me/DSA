def index_print(arr):
    start = -1 
    end = -1 
    sum = 0 
    n = float("-inf")
    for i in range(len(arr)):
        if sum == 0:
            istart = i 
        sum += arr[i] 
        if sum > n:
            n = sum
            end = i 
            start = istart
        if sum < 0:
            sum = 0 
        
    return start,end 
arr = [-2,-3,4,-1,-2,1,5,-3]
print(index_print(arr))