nums= [1,2,3,4]
k = 1
c = nums.copy()
for i in range(len(nums)):
    nums[(i+k) % len(nums)] = c[i]

print(nums)