def remove_duplicates(arr):
    pointer = 0
    for i in range(1, len(arr)):
        if(arr[i] != arr[pointer] and (pointer + 1) < len(arr)):
            arr[pointer+1] = arr[i]
            pointer += 1
    return pointer + 1
print(remove_duplicates([2, 2, 2, 11]))
