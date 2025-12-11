def brute(nums,t):
    cnt = 0 
    k = 0
    for i in range(len(nums)-1):
        if nums[k] == t: 
            cnt += 1
        k +=1 
        if nums[i] + nums[k] == t: 
            cnt += 1

    return cnt
            

def better(nums,t):
    cnt = 0 
    for i in range(len(nums)):
        sum = 0 
        for j in range(i, len(nums)):
            sum += nums[j] 
            if sum == t:
                cnt += 1
    return cnt

def optimal(nums, t): 
    d = {0:1} 
    cnt = 0 
    s = 0
    for i in range(len(nums)): 
        s += nums[i] 
        if s-t in d: 
            cnt = d[s-t] +1
        d[nums[i]] = 1 

    return cnt
nums = [1,2,1,1]
print(optimal(nums,3))
