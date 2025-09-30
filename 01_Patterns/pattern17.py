ch = 'E'
n = 5

for i in range(n): 
    for j in range(ord(ch)-i, ord(ch)+1):
        print(chr(j), end = "")
    print("")