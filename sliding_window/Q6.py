def no_repeat_substring(arr):
    start, end = 0, 0
    max_string = 0
    hash_map = {}
    for end in range(len(arr)):
        right_char = arr[end]
        if right_char not in hash_map:
            hash_map[right_char] = 1
        else:
            start = end
        max_string = max(max_string, end - start + 1)
    return max_string

print(no_repeat_substring("abccde"))