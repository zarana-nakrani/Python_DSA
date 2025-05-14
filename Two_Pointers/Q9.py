def dutch_national_flag(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] == 1:
            if arr[start + 1] != 1:
                arr[start + 1], arr[start] = arr[start], arr[start + 1]
            else:
                start += 1
        elif arr[start] == 2:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
        else:
            start += 1
    return arr

print(dutch_national_flag([1, 0, 2, 1, 0]))