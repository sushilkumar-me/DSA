def brute_soultion(arr):
    k = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            s = arr[j]-arr[i]
            if s>k:
                k = s 
    return k
def better_solution(arr):
    mini = arr[0]
    profit =0
    for i in range(1, len(arr)):
        cost = arr[i] - mini 
        profit = max(cost, profit)
        mini = min(mini, arr[i])
    return profit

arr = [7,1,5,3,6,4]
print(brute_soultion(arr))
print(better_solution(arr))