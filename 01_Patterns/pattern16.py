n = 5
ch = 'A' 
for i in range(n):
    # space  
    for j in range(n-i-1):
        print(" ", end="")

    for j in range(ord(ch), ord(ch)+i+1): 
        print(chr(j), end="") 
        
    # reverse part
    for j in range(ord(ch)+i-1, ord(ch)-1, -1): 
        print(chr(j), end= "")    
    
    print("")
    
    
        
