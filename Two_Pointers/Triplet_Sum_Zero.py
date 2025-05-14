def triplet_sum_to_zero(arr):
    arr.sort()
    print(arr)
    count = 0
    for i in range(0,len(arr)):
        requiredSum = 0 - arr[i]
        l = i + 1
        r = len(arr) - 1
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                count += 1
                continue
            elif arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1
    return count

print(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))