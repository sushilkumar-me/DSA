def brute(nums): 
    s = set()
    for i in range(len(nums)): 
        for j in range(i+1,len(nums)): 
            for k in range(j+1, len(nums)): 
                if nums[i] + nums[j] + nums[k] == 0: 
                    t = tuple(sorted([nums[i], nums[j], nums[k]]))
                    s.add(t)

    return [list(tri) for tri in s]
                    

def better(nums): 
    s = set(nums)
    s1 = set()
    for i in range(len(nums)): 
        s.discard(nums[i])
        for j in range(i+1, len(nums)): 
            s.discard(nums[j])
            k = -(nums[i]+nums[j]) 
            if k in s: 
                t = tuple(sorted([nums[i], nums[j], k])) 
                s1.add(t)
            s.add(nums[j]) 
        s.add(nums[i])
    return [list(tre) for tre in s1]

def optimal(nums): 
    nums = sorted(nums)
    s = set() 
    l = []
    for i in range(len(nums)): 
        if i>0 and nums[i] == nums[i-1]: 
            continue 
        j = i+1 
        k = len(nums)-1 
        while j<k: 
            if nums[i]+nums[j]+nums[k] == 0:  
                l.append([nums[i], nums[j], nums[k]])
                j += 1 
                k -= 1
                while j < k and nums[j] == nums[j-1]: 
                    j +=1 
                while j < k and nums[k] == nums[k+1]: 
                    k +=1 
            elif nums[i]+nums[j]+nums[k] < 0: 
                j += 1 
            elif nums[i]+nums[j]+nums[k] > 0: 
                k -= 1
        
    return l
nums = [-1,0,1,2,-1,-4] 
print(better(nums))