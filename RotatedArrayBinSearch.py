"""
what is a rotated array?
lets say we have sorted array
arr = [2, 3,4, 5, 7, 9, 10, 12]
after first clockwise rotation
arr = [12, 2, 3, 4, 5, 7, 9, 10]
after 2nd rotation:
arr = [10, 12, 2, 3, 4, 5, 7, 9]
Ques: find target element in rotated binary search
Approach: 1. find the pivot
                what is pivot?
                arr = [3, 4, 5, 6, 7, 0, 1, 2]
                pivot = 7 or we can say largest element in the array around which elements will be sorted in the ascending order
        2. when pivot is found search for the element in first half => 0 to pivot
        3. if not found in the first half, search in the other half
dividing this problem in small chunk:
how to find pivot?
"""

arr = [3, 4, 5, 6, 7, 0, 1, 2]
target = 5

def rotatedArrayBS(arr, target):
    low = 0
    high = len(arr) - 1
    mid = low + (high - low) // 2
    while low < high and mid + 1 < len(arr) and arr[mid] < arr[mid + 1]:
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            mid = low + (high - low) // 2
            low = mid + 1
        else:
            mid = low + (high - low) // 2
            high = mid - 1
    pivot = mid
    print(pivot)

rotatedArrayBS(arr, target)