def rec(i, sum): 
    if i < 1: 
        print(sum)
        return   
    rec(i-1, sum+i)
    
n = 5 
rec(n,0)