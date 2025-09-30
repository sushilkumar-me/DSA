def Majority(nums):
    d = {} 
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] =1 
        else:
            d[nums[i]] += 1
    for i in d:
        if d[i] > len(nums)//2:
            return i 
nums = [2,2,1,1,1,2,2]
print(Majority(nums))        