from itertools import combinations

friends = ['Alice', 'Bob', 'Charlie']

# Choosing 2 friends (order doesn't matter)
pairs = combinations(friends, 2)

for pair in pairs : 
    print(pair)

# Choosing 3 friends (order doesn't matter)