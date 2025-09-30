def singleNumber(nums):
    k = 0
    for i in nums:
        k ^= i 
    return k 

nums = [2,2,1]
print(singleNumber(nums))
