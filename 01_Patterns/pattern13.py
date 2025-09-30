ch = 'A'
for i in range(5): 
    for j in range(ord(ch), ord(ch) + i + 1): 
        print(chr(j), end="")
    print("")
