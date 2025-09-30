def brute_solution(arr):
    n = float("-inf")
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
                if sum > n:
                    n = sum 
    return n 
# Better solution
def better_solution(arr):
    n = float("-inf")
    for i in range(len(arr)):
        sum = 0 
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum > n:
                n = sum
    return n
## Optimal soultion
def optimal_solution(arr):
    n = float("-inf")
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if n< sum:
            n= sum 
        if sum < 0:
            sum = 0 
    return n
arr = [-2,-3,4,-1,-2,1,5,-3]
print(brute_solution(arr))
print(better_solution(arr))
print(optimal_solution(arr))