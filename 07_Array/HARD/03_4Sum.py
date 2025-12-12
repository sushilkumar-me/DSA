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

def better(nums, target): 
    s1 = set()
    for i in range(len(nums)): 
        for j in range(i+1, len(nums)): 
            s = set()
            for k in range(j+1, len(nums)): 
                l = target-(nums[i]+nums[j]+nums[k]) 
                if l in s: 
                    t  = tuple(sorted([nums[i], nums[j], nums[k], l])) 
                    s1.add(t)
                s.add(nums[k])
    return [list(tre) for tre in s1]

def optimal(nums, target): 
    h = [] 
    nums.sort() 
    for i in range(len(nums)): 
        if i >0 and nums[i] == nums[i-1]: 
            continue 
        for j in range(i+1, len(nums)): 
            if j >i+1 and nums[j] == nums[j-1]: 
                continue 
            k = j+1 
            l = len(nums)-1 
            while k <l: 
                if nums[i]+nums[j]+nums[k]+nums[l] == target: 
                    h.append([nums[i], nums[j], nums[k], nums[l]]) 
                    k += 1
                    l -= 1
                    while k<l and nums[k] == nums[k-1]: 
                        k +=1 
                    while k<l and nums[l] == nums[l+1]: 
                        l -=1 
                elif nums[i]+nums[j]+nums[k]+nums[l] < target: 
                    k +=1 
                else: 
                    l -=1 
    return h

nums = [1,0,-1,0,-2,2]
target = 0
print(optimal(nums, target))