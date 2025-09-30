n = 5 
ispace = 8 
for i in range(n): 
    # stars 
    for j in range(i+1):
        print("*", end="")
    # spaces
    for j in range(ispace):
        print(" ", end="")
    ispace -= 2
    # stars 
    for j in range(i+1): 
        print("*", end="")
    print("")

n = 3 
ispace = 2 
for i in range(n, -1, -1): 
    # stars 
    for j in range(i+1): 
        print("*", end="")
    # spaces
    for j in range(ispace):
        print(" ", end="")
    ispace += 2
    # stars
    for j in range(i+1): 
        print("*", end="")
    print("")