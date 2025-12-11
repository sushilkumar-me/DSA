## Rotate array also check if sorted
def is_sorted(l):
    count = 0
    for i in range(len(l)):
        if l[i] > l[(i +1) % len(l)]:
            count += 1
    if count > 1:
        return False
    return True


l = [2,1,3,4]
print(is_sorted(l))
