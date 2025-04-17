# arr = [5, 3, 4, 1, 2]
# arr = []
arr = [0, -23, 56, 18]
def insertion_sort(arr):
    for j in range(1, len(arr)):
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

insertion_sort(arr)
print(arr)