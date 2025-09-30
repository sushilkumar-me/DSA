a1 = [1,2,3,4]
a2 = [3,4,5,6]

def find_union(arr1, arr2):
    hash_set = set()
    for i in arr1:
        hash_set.add(i)
    for i in arr2:
            hash_set.add(i)
    return list(hash_set)

re=find_union(a1, a2)
print(re)