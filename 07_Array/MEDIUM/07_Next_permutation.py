def NextPer(nums):
    index = -1 
    for i in range(len(nums)-2, -1,-1):
        if nums[i] < nums[i+1]:
            index = i 
            break 
    
    if index == -1:
        j = len(nums)-1
        for i in range(len(nums)//2):
            nums[i], nums[j] = nums[j], nums[i]
            j -=1
        return nums
    
    for i in range(len(nums)-1, index, -1):
        if nums[i] > nums[index]:
            nums[i], nums[index] = nums[index], nums[i] 
            break
    k = len(nums)-1
    for i in range(index+1,(len(nums)+index+1)//2,1):
        nums[i], nums[k] = nums[k], nums[i] 
        k -=1

    return nums


nums = [2,3,0,0,1,4,5]
print(NextPer(nums))