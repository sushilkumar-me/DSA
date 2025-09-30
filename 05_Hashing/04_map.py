arr = [1,2,2,3,3]
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

n = int(input())
print(freq.get(n, 0)) # Print the frequency or 0 if not found

