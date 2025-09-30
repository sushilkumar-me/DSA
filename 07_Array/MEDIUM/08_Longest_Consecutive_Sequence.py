def ls(nums, x):
    for i in range(len(nums)):
        if nums[i] == x: 
            return True 
    return False
def brute(nums):
    longcon = 1 
    for i in range(len(nums)):
        cnt = 1 
        x = nums[i]
        while ls(nums, x+1):
            cnt += 1
            x += 1 
        longcon = max(longcon, cnt)
    return longcon

def better(nums):
    s = list(set(nums))
    s.sort() 
    cnt = 1
    longcnt = 1
    for i in range(len(s)-1):
        
        if s[i]+1 != s[i+1]:
            cnt = 1
        else:
            cnt += 1
        longcnt = max(longcnt, cnt)        
    return longcnt

def optimal(nums):
    if len(nums) == 0:
        return 0 
    longcnt = 1 
    s = set(nums)
    for i in s: 
        if i-1 not in s:
            cnt = 1
            
            while i+1 in s: 
                i += 1
                cnt +=1 
            longcnt = max(longcnt, cnt)
    return longcnt

nums = [100,4,200,1,3,2]
print(optimal(nums))
         
