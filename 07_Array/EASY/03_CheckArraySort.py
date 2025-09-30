## Rotate array also check if sorted
def is_sorted(l):
    count = 0
    for i in range(len(l)-1):
        if l[i] > l[(i +1) % len(l)]:
            count += 1
    if count > 1:
        return False
    return True


l = [3,3,4,4,5,1,2]
print(is_sorted(l))
