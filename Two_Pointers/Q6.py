def triplet_sum_closest_target(arr, target):
    arr.sort()
    smallest_diff = float('-inf')
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            targetDiff = target - (arr[i] + arr[left] + arr[right])
            if targetDiff == 0:
                return target - targetDiff
            if abs(targetDiff) < abs(smallest_diff):
                smallest_diff = targetDiff
            if targetDiff > 0:
                left += 1
            else:
                right -= 1

    return target - smallest_diff

print(triplet_sum_closest_target([-2, 0, 1, 2], 2))
