from collections import defaultdict 

dd = defaultdict(int) # Default value is 0 for int
dd['a'] += 1
print(dd['a'])  # Output: 1
print(dd['b'])  # Output: 0 (not error, default value is used)

## What it is: A special dictionary that gives a default value if a key is missing.
