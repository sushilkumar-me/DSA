def TwoSum(nums, t):
    k = {} 
    for i in range(len(nums)):
        if t-nums[i] in k:
            return k[t-nums[i]], i 
        k[nums[i]] = i

nums = [1,2,3,4]
t = 5
print(TwoSum(nums,t))