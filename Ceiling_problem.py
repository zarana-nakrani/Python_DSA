##Ceiling of a given number => find the smallest number that is greater or equal to the target element
"""
Eg arr = [2, 3, 4, 5, 9, 14, 16, 18] and target = 14
Ceiling(arr, target) = 14
lets say target = 15
Ceiling(arr, target) = 16
if target = 4 =>  Ceiling(arr, target) = 5

Similar question
Floor of a number => greatest number that is smaller or equal to target number
Floor(arr, target=6) => 6
"""
import Binary_Search
arr = [2, 3, 4, 5, 9, 14, 16, 18]
target = 7
def Ceiling(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return arr[mid+1]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return arr[low]

def Floor(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return arr[high]

print(f"Ceiling of a number: {Ceiling(arr, target)}")
print(f"Floor of a number: {Floor(arr, target)}")