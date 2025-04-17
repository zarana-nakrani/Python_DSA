# arr = [5, 4, 3, 2, 1]
# arr = [4,3,2,7,8,2,3,1]
arr = [3,1,3,4,2]
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correctIndex = arr[i] - 1
        if arr[i] != arr[correctIndex]:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
        else:
            i += 1

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # i = 0
    # n = len(nums)
    # while i < n-1:
    #     correctIndex = arr[i]
    #     if arr[i] == n:
    #         arr[i], arr[n - 1] = arr[n - 1], arr[i]
    #     elif arr[i] != i:
    #         arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
    #     else:
    #         i += 1
    # return i
    n = len(nums)
    total = sum(nums)
    sum_nums = (n * (n+1)) / 2
    missing_nums= int(sum_nums - total)
    return missing_nums
# cyclic_sort(arr)

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if nums[i] != i + 1 and nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1
    arr = []
    for j in range(0, len(nums)):
        if nums[j] == j + 1:
            continue
        else:
            arr.append(j + 1)
    return arr

# print(findDisappearedNumbers(arr))

def findOneMissingNumber(nums):
    # i = 0
    # while i < len(nums):
    #     correctIndex = nums[i] -1
    #     if nums[correctIndex] != nums[i]:
    #         nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
    #     else:
    #         i += 1
    #
    # for j in range(len(nums)):
    #     if j != nums[j] - 1:
    #         return nums[j]
    #Another approach
    temp_nums = set(nums)
    diff = sum(nums) - sum(temp_nums)
    missing_num = int(diff / (len(nums) - len(temp_nums)))
    return missing_num
# print(findOneMissingNumber(arr))

def findAllDuplicates(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if nums[correctIndex] != nums[i]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

def firstMissingPositive(nums):
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if 0 < nums[i] <= len(nums) and nums[i] != nums[correctIndex] and correctIndex < len(nums):
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1

    for j in range(len(nums)+1):
        if nums[j] != j + 1:
            return j + 1

    if len(nums) == 1 and nums[0] == 1:
        return 2
    else:
        return 1

print(firstMissingPositive([1]))