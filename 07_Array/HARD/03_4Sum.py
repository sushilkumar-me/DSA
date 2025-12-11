def brute(nums, target): 
    s = set() 
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            for k in range(j+1, len(nums)): 
                for l in range(k+1, len(nums)): 
                    if nums[i]+nums[j]+nums[k]+nums[l] == target: 
                        t = tuple(sorted([nums[i], nums[j], nums[k], nums[l]])) 
                        s.add(t) 

    return [list(tre) for tre in s]
nums = [1,0,-1,0,-2,2]
target = 0
print(brute(nums, target))