
def quadraple_sum_to_target(arr, target):
    arr.sort()
    result = []
    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            diff = target - arr[j] -  arr[i]
            result = helper_function(i, j, arr, diff, result)
    return result



def helper_function(i, j, arr, diff, result):
    left = j + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == diff:
            result.append([arr[i], arr[j], arr[left], arr[right]])
            left += 1
            right -= 1
        elif arr[left] + arr[right] < diff:
            left += 1
        else:
            right -= 1

    return result

print(quadraple_sum_to_target([2, 0, -1, 1, -2, 2], 1))