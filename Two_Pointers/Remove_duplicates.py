from itertools import count


def remove_dupes(arr):
    start = 0
    end = 0
    while end < len(arr):
        if arr[start] != arr[end]:
            arr[start + 1], arr[end] = arr[end], arr[start + 1]
            end += 1
            start += 1
        else:
            end += 1
    return (start - 0) + 1

# print(remove_dupes([2, 2, 2, 11]))


def remove_keys(arr, key):
    count = 0
    for i in range(len(arr)):
        if arr[i] == key:
            count += 1
    return len(arr) - count

print(remove_keys([2, 11, 2, 2, 1], 2))