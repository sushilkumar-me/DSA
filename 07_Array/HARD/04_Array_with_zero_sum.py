def brute(nums): 
    p = 0
    k =0
    for i in range(len(nums)): 
        s = 0
        for j in range(i,len(nums)):
            k += nums[j]
            if k == 0:
                s = j-i+1
                print(s)
            if p < s: 
                p = s 

    return p

nums= [15, -2, 2, -8, 1, 7, 10, 23]
print(brute(nums))