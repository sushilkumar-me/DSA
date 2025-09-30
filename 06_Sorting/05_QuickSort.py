def qs(arr, low, high):
    if low < high:
        partition = f(arr, low, high)
        qs(arr, low, partition - 1)
        qs(arr, partition + 1, high)


def f(arr, low, high):
    pivot = arr[low]
    i = low 
    j = high
    while i < j:
        while arr[i] <= arr[pivot] and i <= high:
            i += 1
        while arr[j] > arr[pivot] and j >= low:
            j -= 1
        arr[low], arr[j] = arr[j], arr[low]
        return j

def quickSort(arr, n):
    qs(arr, 0, n - 1)

arr = [2, 7, 4, 1]
n = len(arr)
quickSort(arr, n)
print(arr)  