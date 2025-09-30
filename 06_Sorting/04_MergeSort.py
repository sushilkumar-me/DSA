def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mS(arr, low, high): 
    if low >= high:
        return 
    mid = (low + high) // 2
    mS(arr, low, mid)
    mS(arr, mid + 1, high)
    merge(arr, low, mid, high)

def mergeSort(arr, n):
    mS(arr, 0, n - 1)

arr = [2, 7, 4, 1]
n = len(arr)
mergeSort(arr, n)
print(arr)   # Output should be: [1, 2, 4, 7]
