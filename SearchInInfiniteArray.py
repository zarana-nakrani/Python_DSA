def search_infinite_array(arr, low, high, len, target):
    try:
        while target > arr[high]:
            low = high + 1
            len *= 2
            high = high + len
            print(high)
        while low <= high:
            print(high)
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    except IndexError:
        len = len // 2
        high = high - len
        if high < low:
            return -1
        else:
            search_infinite_array(arr, low, high, len, target)


arr = [2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 20, 23, 30]
target = 15
len = 2
low = 0
high = low + len
result = search_infinite_array(arr, low, high, len, target)
if result != -1 :
    print(result)
else:
    print("Element not found in infinite array")
