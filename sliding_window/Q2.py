

def smallest_subarray(arr, S):
    sum, previous, i, length = 0, 0, 0, 0
    result = len(arr)
    while i < len(arr) or sum >= S:
        if sum >= S:
            length = i - previous
            sum -= arr[previous]
            previous += 1
            if length < result:
                result = length
        else:
            sum += arr[i]
            i += 1

    return result

# print(smallest_subarray([2, 1, 5, 2, 3, 2], S=7))
print(smallest_subarray([3, 4, 1, 1, 6], S=8 ))