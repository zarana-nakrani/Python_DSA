"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
"""
def triplet_sum_smaller(arr, target):
    arr.sort()
    print(arr)
    count = 0
    nums = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        target_diff = target - arr[i]
        while left < right:

            if arr[left] + arr[right] < target_diff:
                # right -= 1
                count += right - left
                nums.append([arr[i], arr[left], arr[right]])
                left += 1
            else:
                right -= 1

    print(nums)
    return count

print(triplet_sum_smaller([-1, 0, 2, 3], 3))