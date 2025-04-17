def sliding_window(arr, size):
    sum  = 0
    result = 0
    previous = 0
    for i in range(0, len(arr)):
        sum += arr[i]
        if i >= (size - 1):
            if sum > result:
                result = sum
            sum -= arr[previous]
            previous += 1
    return result
print( sliding_window([2, 1, 5, 1, 3, 2], size=3))

