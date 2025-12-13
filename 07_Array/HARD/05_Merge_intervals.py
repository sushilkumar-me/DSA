def optimal(intervals): 
    intervals.sort() 
    
    l = [] 
    l.append(intervals[0]) 
    
    for i in range(1,len(intervals)): 
        if l[len(l)-1][1] >= intervals[i][0]: 
            if l[len(l)-1][1] < intervals[i][1]: 
                l[len(l)-1][1] = intervals[i][1] 
                
        else: 
            l.append(intervals[i]) 

    return l 

intervals = [[1,4],[0,2],[3,5]]
print(optimal(intervals))
            