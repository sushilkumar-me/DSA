def brute(nums): 
    s = 0
    for i in range(len(nums)): 
        k = 0
        for j in range(i,len(nums)):
            
            k += nums[j]
            if k == 0:
                s = max(s,j-i+1)
            
    return s
def optimal(nums): 
    d = {} 
    ma = 0 
    s = 0 
    for i in range(len(nums)): 
        s += nums[i] 
        if s == 0: 
            ma = i+1
        else: 
            if s not in d: 
                d[s]= i
            else: 
                ma = max(ma, i-d[s])
    return ma




nums= [15, -2, 2, -8, 1, 7, 10, 23]
print(brute(nums))