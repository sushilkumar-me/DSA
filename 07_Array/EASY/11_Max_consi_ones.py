l = [1,1,0,1,1,1,0,1,1]
def max_consecutive_ones(l):
    max_count = 0 
    cnt = 0 
    for i in l:
        
        if i == 1:
            cnt += 1 
            max_count = max(max_count, cnt)
        else:
            cnt = 0 
        
        
    return max_count

re = max_consecutive_ones(l)
print(re)