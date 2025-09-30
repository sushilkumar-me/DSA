n = 5
ch = 'A'
for i in range(n, 0, -1): 
    for j in range(ord(ch), ord(ch) + i , +1): 
        print(chr(j), end= "")
    print("")

