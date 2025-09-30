def printname(i, n): 
    if i > n: # Base case: if i exceeds n, stop recursion
        return
    print("Sushil")
    printname(i+1, n)

n = int(input("Enter a number: "))
i = 1
printname(i, n)